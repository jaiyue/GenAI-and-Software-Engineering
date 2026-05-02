import json
import os
import subprocess
import sys
import time

import requests
from decouple import config


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(BASE_DIR)
HUMAN_RESULTS_ROOT = os.path.join(PROJECT_ROOT, "human_results")
URL = "http://localhost:9000/"
TEST_COUNT = 164


def authenticate(url):
    session = requests.Session()
    session.auth = (config("SONAR_TOKEN"), "")
    session.post(url + "api/user_tokens/search")
    session.get(url + "api")
    return session


def create_project(session, project_name, project_key):
    obj = {"name": project_name, "project": project_key}
    return session.post(URL + "api/projects/create", data=obj)


def create_projects(session, name):
    for i in range(TEST_COUNT):
        project_name = name + "_" + str(i)
        project_key = name + "_" + str(i)
        create_project(session, project_name, project_key)
    print("SONARQUBE Created projects")


def run_sonarqube(name):
    token = config("SONAR_TOKEN")
    scanner_path = os.path.join(
        PROJECT_ROOT,
        "sonar-scanner-8.0.1.6346-macosx-aarch64",
        "bin",
        "sonar-scanner",
    )
    for i in range(TEST_COUNT):
        project_key = name + "_" + str(i)
        py_file_name = f"/canonical_solution_{i}.py"
        source_dir = os.path.join(HUMAN_RESULTS_ROOT, str(i))

        cmd = (
            f"{scanner_path} -D'sonar.projectKey={project_key}' "
            f"-D'sonar.sources={source_dir}' "
            f"-D'sonar.inclusions=**{py_file_name}' "
            f"-Dsonar.scm.exclusions.disabled=true"
        )
        cmd += " -D'sonar.host.url=http://localhost:9000'"
        cmd += f" -D'sonar.login={token}'"

        p = subprocess.Popen(["/bin/bash", "-c", cmd], stdout=sys.stdout)
        p.communicate()


def delete_projects(session):
    projects = ""
    project_name = "project"
    for i in range(TEST_COUNT):
        projects += project_name + "_" + str(i) + ","

    obj = {"projects": projects}
    print("SONARQUBE Deleting projects...")
    return session.post(URL + "api/projects/bulk_delete", data=obj)


def get_measures(session, project_key):
    obj = {
        "component": project_key,
        "metricKeys": "code_smells,bugs,security_rating,reliability_rating,sqale_rating,vulnerabilities,security_hotspots",
    }
    return session.get(URL + "api/measures/component", params=obj)


def wait_for_measures(session, project_key, timeout_sec=90, interval_sec=2):
    start_time = time.time()
    last_payload = {"component": {"measures": []}}
    while time.time() - start_time <= timeout_sec:
        measures_response = get_measures(session, project_key)
        try:
            payload = json.loads(measures_response.text)
        except Exception:
            payload = {"component": {"measures": []}}

        last_payload = payload
        component = payload.get("component", {}) if isinstance(
            payload, dict) else {}
        measures = component.get("measures", []) if isinstance(
            component, dict) else []
        if measures:
            return payload

        time.sleep(interval_sec)

    return last_payload


def save_measures_to_json(session, name):
    os.makedirs(HUMAN_RESULTS_ROOT, exist_ok=True)
    for i in range(TEST_COUNT):
        sample_dir = os.path.join(HUMAN_RESULTS_ROOT, str(i))
        os.makedirs(sample_dir, exist_ok=True)
        project_key = name + "_" + str(i)
        measures = wait_for_measures(session, project_key)
        with open(os.path.join(sample_dir, f"sonar_{i}.json"), "w", encoding="utf-8") as outfile:
            json.dump(measures, outfile)


def extract_metrics(idx):
    metrics = []
    with open(os.path.join(HUMAN_RESULTS_ROOT, str(idx), f"sonar_{idx}.json"), encoding="utf-8") as json_file:
        data = json.load(json_file)
        for p in data["component"]["measures"]:
            metrics.append({p["metric"]: p["value"]})
    return metrics


def extract_all_metrics_to_csv():
    from csv import reader, writer

    all_metrics = []
    for i in range(TEST_COUNT):
        all_metrics.append(extract_metrics(i))

    results_csv = os.path.join(HUMAN_RESULTS_ROOT, "results.csv")
    try:
        with open(results_csv, "r", encoding="utf-8") as f:
            csv_reader = reader(f)
            matrix = [row for row in csv_reader if row != []]
    except FileNotFoundError:
        matrix = [["ID", "Correctness", "Validity", "security_rating", "bugs", "code_smells",
                   "reliability_rating", "vulnerabilities", "security_hotspots",
                   "maintainability_rating"]]
        for i in range(TEST_COUNT):
            matrix.append([str(i), "N/A", "N/A", "N/A", "N/A",
                           "N/A", "N/A", "N/A", "N/A", "N/A"])

    for i in range(TEST_COUNT):
        if all_metrics[i]:
            for metric_dict in all_metrics[i]:
                for key, value in metric_dict.items():
                    if key == "security_rating" and len(matrix[i + 1]) > 3:
                        matrix[i + 1][3] = value
                    elif key == "bugs" and len(matrix[i + 1]) > 4:
                        matrix[i + 1][4] = value
                    elif key == "code_smells" and len(matrix[i + 1]) > 5:
                        matrix[i + 1][5] = value
                    elif key == "reliability_rating" and len(matrix[i + 1]) > 6:
                        matrix[i + 1][6] = value
                    elif key == "vulnerabilities" and len(matrix[i + 1]) > 7:
                        matrix[i + 1][7] = value
                    elif key == "security_hotspots" and len(matrix[i + 1]) > 8:
                        matrix[i + 1][8] = value
                    elif key == "sqale_rating" and len(matrix[i + 1]) > 9:
                        matrix[i + 1][9] = value

    with open(results_csv, "w", newline="", encoding="utf-8") as f:
        csv_writer = writer(f)
        csv_writer.writerows(matrix)

    print("saved human_results/results.csv")


def run_sonarqube_eval():
    project_name = "project"
    session = authenticate(URL)
    delete_projects(session)
    create_projects(session, project_name)
    run_sonarqube(project_name)
    save_measures_to_json(session, project_name)
    extract_all_metrics_to_csv()
