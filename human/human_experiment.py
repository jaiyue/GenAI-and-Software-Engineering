from shared_funcs import get_json_object
from sonarqube import run_sonarqube_eval
import json
import os
import shutil
import sys
from urllib.error import URLError
from urllib.request import urlopen


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(BASE_DIR)
sys.path.insert(0, BASE_DIR)
sys.path.insert(1, PROJECT_ROOT)


NUMBER_OF_SAMPLES = 164
INPUT_ROOT = os.path.join(PROJECT_ROOT, "experiment-code")
OUTPUT_ROOT = os.path.join(PROJECT_ROOT, "human_results")
SONARQUBE_STATUS_URL = "http://localhost:9000/api/system/status"


def write_to_csv_validity_only():
    print("Start validity")
    execute_all_python_files()

    invalid_count = 0
    for i in range(NUMBER_OF_SAMPLES):
        out_path = os.path.join(OUTPUT_ROOT, str(i), "output_validity.txt")
        if not os.path.exists(out_path):
            continue
        with open(out_path, "r", encoding="utf-8") as f:
            contents = f.read().splitlines()
        first_line = contents[0] if contents else ""
        if len(contents) == 0 or "Invalid" in first_line:
            invalid_count += 1
            print("Invalid " + str(i))

    print("Number of Invalid: " + str(invalid_count))
    print("Validity: " + str((NUMBER_OF_SAMPLES - invalid_count) / NUMBER_OF_SAMPLES))
    print("End validity")


def load_func(module_path, entry_point, name):
    spec = __import__("importlib.util").util.spec_from_file_location(
        name, module_path)
    mod = __import__("importlib.util").util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return getattr(mod, entry_point)


def execute_all_python_files():
    print("Scripts running...")
    for i in range(NUMBER_OF_SAMPLES):
        task_dir = os.path.join(OUTPUT_ROOT, str(i))
        inputs_path = os.path.join(INPUT_ROOT, str(i), f"inputs_{i}.json")
        canonical_output_path = os.path.join(
            task_dir, f"canonical_solution_{i}.py")
        canon_path = os.path.join(INPUT_ROOT, str(
            i), f"canonical_solution_{i}.py")
        out_path = os.path.join(task_dir, "output_validity.txt")
        invalid = False

        try:
            with open(inputs_path, "r", encoding="utf-8") as f:
                inputs_obj = json.load(f)
        except Exception as e:
            print(f"{canonical_output_path} -> Inputs load error: {e}")
            print("  Continuing to next sample...")
            continue

        try:
            os.makedirs(task_dir, exist_ok=True)
            shutil.copy2(canon_path, canonical_output_path)
            cand_func = load_func(canonical_output_path,
                                  inputs_obj["entry_point"], f"cand_{i}")
        except Exception as e:
            print(f"{canonical_output_path} -> Candidate import error: {e}")
            invalid = True
            print("  Continuing to next sample...")
            continue

        try:
            ref_func = load_func(
                canon_path, inputs_obj["entry_point"], f"ref_{i}")
        except Exception as e:
            print(f"{canonical_output_path} -> Canonical import error: {e}")
            print("  Continuing to next sample...")
            continue

        cases = inputs_obj["base_input"] + inputs_obj["plus_input"]
        failed_cases = []
        for idx, args in enumerate(cases):
            try:
                cand_func(*args)
            except Exception as e:
                invalid = True
                failed_cases.append({"index": idx, "args": repr(
                    args), "reason": f"candidate_error: {e}"})

        if invalid:
            result_str = "Invalid"
            if failed_cases:
                result_str += " | failed_cases=" + repr(failed_cases)
        else:
            result_str = "Valid"

        with open(out_path, "w", encoding="utf-8") as output:
            output.write(result_str)
        if invalid or failed_cases:
            print(f"{canonical_output_path} -> {result_str}")
    print("Script run completed.")


def prepare_canonical_code():
    for i in range(NUMBER_OF_SAMPLES):
        canon_path = os.path.join(INPUT_ROOT, str(
            i), f"canonical_solution_{i}.py")
        out_dir = os.path.join(OUTPUT_ROOT, str(i))
        out_path = os.path.join(out_dir, f"canonical_solution_{i}.py")

        if not os.path.exists(canon_path):
            print(f"Skip {i}: missing canonical solution")
            continue

        os.makedirs(out_dir, exist_ok=True)
        shutil.copy2(canon_path, out_path)

    missing = []
    for idx in range(NUMBER_OF_SAMPLES):
        copied_path = os.path.join(OUTPUT_ROOT, str(
            idx), f"canonical_solution_{idx}.py")
        if not os.path.exists(copied_path):
            missing.append(idx)
    if missing:
        print(f"Missing canonical files: {missing}")


def is_sonarqube_available():
    try:
        with urlopen(SONARQUBE_STATUS_URL, timeout=3) as response:
            payload = json.loads(response.read().decode("utf-8"))
        return payload.get("status") == "UP"
    except (URLError, TimeoutError, json.JSONDecodeError, ValueError, OSError):
        return False


if __name__ == "__main__":
    prepare_canonical_code()
    write_to_csv_validity_only()
    if is_sonarqube_available():
        run_sonarqube_eval()
    else:
        print(
            f"Skip SonarQube: server is not available at {SONARQUBE_STATUS_URL}")
