import os
import json
import string
# from sonarqube import run_sonarqube_eval
from shared_funcs import get_json_object


NUMBER_OF_SAMPLES = 164


# write validity and correctness to csv file
def write_to_csv_correctness_validity():
    from csv import reader, writer

    print("Start correctness and validity")
    execute_all_python_files()
    test_count = count_test_cases()

    matrix = []
    with open("results/results.csv", "r") as f:
        csv_reader = reader(f)
        for row in csv_reader:
            matrix.append(row)

    sum_score = 0
    inv = 0

    for i in range(NUMBER_OF_SAMPLES):
        out_path = os.path.join("experiment-code", str(i),
                                "output_correctness_validity.txt")
        if not os.path.exists(out_path):
            continue
        with open(out_path, 'r') as f:
            contents = f.read().splitlines()
        if len(contents) == 0 or "Invalid" in contents:
            inv = inv + 1
            matrix[i + 1][2] = 0
            print("Invalid" + " " + str(i))
        else:
            # Extract the number part before any ' |' separator
            num_str = contents[0].split(' |')[0].strip()
            correct = float(num_str)
            ratio = correct / float(test_count[i])
            matrix[i + 1][2] = 1
            if ratio < 1:
                print(str(i) + " Correct: " + str(correct) + " Total: " +
                      str(test_count[i]) + " Ratio: " + str(ratio))
            matrix[i + 1][1] = ratio
            sum_score = sum_score + ratio
    print("Number of Invalid: " + str(inv))
    print("SUM: " + str(sum_score / (NUMBER_OF_SAMPLES -
          inv if NUMBER_OF_SAMPLES - inv else 1)))

    with open("results/results.csv", "w", newline='') as f:
        writer = writer(f)
        for row in matrix:
            writer.writerow(row)

    print("End correctness and validity")


def load_func(module_path, entry_point, name):
    spec = __import__("importlib.util").util.spec_from_file_location(
        name, module_path)
    mod = __import__("importlib.util").util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return getattr(mod, entry_point)

# Execute all python files with prompt


def execute_all_python_files():
    print("Scripts running...")
    for i in range(NUMBER_OF_SAMPLES):
        task_dir = os.path.join("experiment-code", str(i))
        inputs_path = os.path.join(task_dir, f"inputs_{i}.json")
        merged_path = os.path.join(task_dir, f"merged_{i}.py")
        canon_path = os.path.join(task_dir, f"canonical_solution_{i}.py")
        out_path = os.path.join(task_dir, "output_correctness_validity.txt")
        invalid = False

        # load inputs
        try:
            with open(inputs_path, "r", encoding="utf-8") as f:
                inputs_obj = json.load(f)
        except Exception as e:
            print(f"{merged_path} -> Inputs load error: {e}")
            print(f"  Continuing to next sample...")
            continue

        # load candidate
        try:
            cand_func = load_func(
                merged_path, inputs_obj["entry_point"], f"cand_{i}")
        except Exception as e:
            print(f"{merged_path} -> Candidate import error: {e}")
            invalid = True
            print(f"  Continuing to next sample...")
            continue

        # load canonical
        try:
            ref_func = load_func(
                canon_path, inputs_obj["entry_point"], f"ref_{i}")
        except Exception as e:
            print(f"{merged_path} -> Canonical import error: {e}")
            print(f"  Continuing to next sample...")
            continue

        cases = inputs_obj["base_input"] + inputs_obj["plus_input"]
        atol = inputs_obj["atol"]
        count = 0
        failed_args = None
        for args in cases:
            try:
                ref_out = ref_func(*args)
            except Exception:
                break
            try:
                out = cand_func(*args)
            except Exception:
                invalid = True
                failed_args = args
                break
            try:
                if atol is not None and isinstance(out, (int, float)) and isinstance(ref_out, (int, float)):
                    ok = abs(out - ref_out) <= atol
                else:
                    ok = out == ref_out
            except Exception:
                ok = out == ref_out
            if ok:
                count += 1
            else:
                failed_args = args
                break

        if invalid:
            result_str = "Invalid"
        else:
            result_str = str(count)
            if failed_args is not None:
                result_str = result_str + " | failed_args=" + repr(failed_args)
        with open(out_path, 'w') as output:
            output.write(result_str)
        if invalid or failed_args is not None:
            print(f"{merged_path} -> {result_str}")
    print("Script run completed.")


# Count number of test cases for each problem
def count_test_cases():
    test_count = []
    os.chdir('experiment-code')
    for i in range(NUMBER_OF_SAMPLES):
        os.chdir(str(i))
        try:
            inputs_obj = get_json_object("inputs_" + str(i))
            cases = inputs_obj["base_input"] + inputs_obj["plus_input"]
            test_count.append(len(cases))
        except Exception:
            test_count.append(0)
        os.chdir('..')
    os.chdir('..')
    return test_count


def merge_code():
    # Merge prompt and generated code for each task into experiment-code/{i}/merged_{i}.py, de-duplicating lines.
    for i in range(NUMBER_OF_SAMPLES):
        prompt_path = os.path.join("code_generation", str(i), f"prompt_{i}.py")
        gen_path = os.path.join("python_code", f"code_{i}.py")
        out_dir = os.path.join("experiment-code", str(i))
        out_path = os.path.join(out_dir, f"merged_{i}.py")

        if not (os.path.exists(prompt_path) and os.path.exists(gen_path)):
            print(f"Skip {i}: missing prompt or generated code")
            continue

        with open(prompt_path, "r", encoding="utf-8", errors="ignore") as f:
            prompt_lines = f.readlines()
        with open(gen_path, "r", encoding="utf-8", errors="ignore") as f:
            code_lines = f.readlines()

        # trim generated code
        python_symbols = set(
            string.ascii_letters
            + string.digits
            + "_ \t\r\n()[]{}.,:;+-*/%<>=!&|^~@#\\'\"≡"
        )
        filtered_code = []
        skip_mode = True  # Start in skip mode until we find import/from/def
        for line in code_lines:
            stripped = line.lstrip()

            if skip_mode:
                # In skip mode: look for import/from/def to start keeping code
                if (stripped.startswith("import ") or
                    stripped.startswith("from ") or
                        stripped.startswith("def ")):
                    skip_mode = False  # Enter keep mode
                    filtered_code.append(line)
                    continue
                else:
                    continue  # Stay in skip mode
            else:
                # In keep mode: check if we should switch back to skip mode
                if line and not line[0].isspace():
                    if line[0].isupper() or (not line[0].isalpha() and line[0] != "_"):
                        skip_mode = True  # Switch back to skip mode
                        continue

                # Additional filters for kept code
                # if "->" in line:
                #     continue
                # if any(word not in python_symbols for word in line):
                #     continue

                filtered_code.append(line)

        # Add import/from and def lines from prompt that are not already in filtered_code
        import_code = []
        in_def = False
        for line in prompt_lines:
            stripped = line.lstrip()

            # Add import/from lines
            if (stripped.startswith("import ") or stripped.startswith("from ")) and not line[0].isspace():
                if line not in filtered_code:
                    import_code.append(line)

            # Start def block
            elif stripped.startswith("def "):
                # Extract function name to avoid duplicates
                func_name = stripped.split('(')[0].replace('def ', '').strip()
                func_exists = any(
                    f"def {func_name}" in l for l in filtered_code)

                if not func_exists:
                    import_code.append(line)
                    in_def = True

            # Continue or stop def block
            elif in_def:
                if line.strip() == "":  # Empty line stops the def block
                    in_def = False
                else:
                    import_code.append(line)

        merged = import_code + filtered_code

        os.makedirs(out_dir, exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            f.writelines(merged)

    # Verify merged files for indices 0-164 exist; report any missing.
    missing = []
    for idx in range(164):
        merged_path = os.path.join(
            "experiment-code", str(idx), f"merged_{idx}.py")
        if not os.path.exists(merged_path):
            missing.append(idx)
    if missing:
        print(f"Missing merged files: {missing}")


merge_code()
write_to_csv_correctness_validity()
