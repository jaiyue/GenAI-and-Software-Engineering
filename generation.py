# Input:
#   - Prompts loaded from files: code_generation/<test_id>/prompt_*.py
# Output:
#   - Generated python files at python_code/code_<test_id>.py

import os
import shutil
import subprocess
import glob

# Generate code using Copilot CLI
def generate_code_with_copilot(prompt: str) -> str:
    result = subprocess.run(
        ["copilot", "-p", prompt],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        raise RuntimeError(result.stderr)

    if not result.stdout.strip():
        raise RuntimeError(
            "Copilot returned empty output.\n"
            f"stderr:\n{result.stderr}"
        )

    return result.stdout

# Load prompts from code_generation/<test_id>/prompt_*.py
def load_test_cases(prompt_root: str) -> dict:
    test_cases = {}

    for test_id in os.listdir(prompt_root):
        test_dir = os.path.join(prompt_root, test_id)
        if not os.path.isdir(test_dir):
            continue

        prompt_files = glob.glob(os.path.join(test_dir, "prompt_*.py"))
        if not prompt_files:
            continue

        with open(prompt_files[0], "r", encoding="utf-8") as f:
            test_cases[test_id] = f.read()

    return test_cases


# Generate code files for all test cases
def generate_all_codes(test_cases: dict, output_root: str):
    # Remove existing output directory if it exists
    if os.path.exists(output_root):
        shutil.rmtree(output_root)

    os.makedirs(output_root, exist_ok=True)

    for test_id, prompt in test_cases.items():
        code = generate_code_with_copilot(prompt)

        output_file = os.path.join(output_root, f"code_{test_id}.py")
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(code)


# Main execution
if __name__ == "__main__":
    prompt_root = "code_generation"
    output_root = "python_code"

    test_cases = load_test_cases(prompt_root)
    generate_all_codes(test_cases, output_root)
