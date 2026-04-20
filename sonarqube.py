import json
import requests
import pprint
import os
from requests.sessions import session
import subprocess
import sys
import time
from decouple import config


url = 'http://localhost:9000/'
TEST_COUNT = 164


# Authenticate
def authenticate(url):
    session = requests.Session()
    # use token auth
    session.auth = (config("SONAR_TOKEN"), '')

    auth = session.post(url + 'api/user_tokens/search')
    response = session.get(url + 'api')

    return session


# Create a sonarqube project
def create_project(session, project_name, project_key):
    obj = {'name': project_name, 'project': project_key}
    response = session.post(url + 'api/projects/create', data=obj)

    return response


# create projects
def create_projects(session, name):
    for i in range(TEST_COUNT):
        project_name = name + "_" + str(i)
        project_key = name + "_" + str(i)
        create_project(session, project_name, project_key)
    print('SONARQUBE Created projects')


def run_sonarqube(name):
    token = config("SONAR_TOKEN")
    # scanner path
    scanner_path = "sonar-scanner-8.0.1.6346-macosx-aarch64/bin/sonar-scanner"
    for i in range(TEST_COUNT):
        project_key = name + "_" + str(i)
        # merged source file
        py_file_name = "/merged_" + str(i) + ".py"
        source_dir = f"experiment-code/{i}"

        # run scanner
        cmd = f"{scanner_path} -D'sonar.projectKey={project_key}' -D'sonar.sources={source_dir}' -D'sonar.inclusions=**{py_file_name}' -Dsonar.scm.exclusions.disabled=true"
        # add host and token
        cmd += " -D'sonar.host.url=http://localhost:9000'"
        cmd += f" -D'sonar.login={token}'"

        p = subprocess.Popen(["/bin/bash", "-c", cmd], stdout=sys.stdout)
        p.communicate()


# Delete a sonarqube project
def delete_projects(session):
    projects = ""
    project_name = "project"
    for i in range(TEST_COUNT):
        projects += project_name + "_" + str(i) + ","

    obj = {'projects': projects}
    print('SONARQUBE Deleting projects...')
    response = session.post(url + 'api/projects/bulk_delete', data=obj)
    return response


# get measures
def get_measures(session, project_key):
    obj = {
        'component': project_key,
        'metricKeys': 'code_smells,bugs,security_rating,reliability_rating,sqale_rating,vulnerabilities,security_hotspots'
    }
    measures_response = session.get(url + 'api/measures/component', params=obj)
    return measures_response


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


# save all measures
def save_measures_to_json(session, name):
    os.chdir('experiment-results')

    for i in range(TEST_COUNT):
        os.chdir(str(i))
        project_key = name + "_" + str(i)
        measures = wait_for_measures(session, project_key)
        with open('sonar_' + str(i) + '.json', 'w') as outfile:
            json.dump(measures, outfile)
        os.chdir('..')
    os.chdir('..')


# Extract metrics for one problem
def extract_metrics(idx):
    metrics = []
    with open('sonar_' + str(idx) + '.json') as json_file:
        data = json.load(json_file)
        metric = []
        print(data)
        for p in data['component']['measures']:
            metric.append(p['metric'])
            metric.append(p['value'])
            metric_key_value = {}
            metric_key_value[p['metric']] = p['value']
            metrics.append(metric_key_value)
            metric = []
    return metrics


# Save all metrics
def extract_all_metrics_to_csv():
    from csv import reader, writer

    allMetrics = []
    os.chdir('experiment-results')
    for i in range(TEST_COUNT):
        os.chdir(str(i))
        allMetrics.append(extract_metrics(i))
        os.chdir('..')
    os.chdir('..')

    # load csv
    try:
        with open("results/results.csv", "r") as f:
            csv_reader = reader(f)
            matrix = [row for row in csv_reader if row != []]
    except FileNotFoundError:
        # init csv
        matrix = [['ID', 'Correctness', 'Validity', 'security_rating', 'bugs', 'code_smells',
                   'reliability_rating', 'vulnerabilities', 'security_hotspots',
                   'maintainability_rating']]
        for i in range(TEST_COUNT):
            matrix.append([str(i), "N/A", "N/A", "N/A", "N/A",
                          "N/A", "N/A", "N/A", "N/A", "N/A"])

    # fill metrics
    for i in range(TEST_COUNT):
        if allMetrics[i] and len(allMetrics[i]) > 0:
            for metric_dict in allMetrics[i]:
                for key, value in metric_dict.items():
                    # map columns
                    if key == 'security_rating' and len(matrix[i+1]) > 3:
                        matrix[i+1][3] = value
                    elif key == 'bugs' and len(matrix[i+1]) > 4:
                        matrix[i+1][4] = value
                    elif key == 'code_smells' and len(matrix[i+1]) > 5:
                        matrix[i+1][5] = value
                    elif key == 'reliability_rating' and len(matrix[i+1]) > 6:
                        matrix[i+1][6] = value
                    elif key == 'vulnerabilities' and len(matrix[i+1]) > 7:
                        matrix[i+1][7] = value
                    elif key == 'security_hotspots' and len(matrix[i+1]) > 8:
                        matrix[i+1][8] = value
                    elif key == 'sqale_rating' and len(matrix[i+1]) > 9:
                        matrix[i+1][9] = value

    # save csv
    with open("results/results.csv", "w", newline='') as f:
        writer = writer(f)
        writer.writerows(matrix)

    print("saved results/results.csv")


def run_sonarqube_eval():
    project_name = "project"
    session = authenticate(url)
    delete_projects(session)
    create_projects(session, project_name)
    run_sonarqube(project_name)
    save_measures_to_json(session, project_name)
    extract_all_metrics_to_csv()
