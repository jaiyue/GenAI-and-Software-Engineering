# GenAI-and-Software-Engineering

## HumanEvalPlus-Mini Dataset Extraction Guide

This section describes how to obtain the **HumanEvalPlus-Mini** dataset from the EvalPlus framework **without performing any model evaluation or program execution**.

### Step 1: Clone the EvalPlus Repository

```bash
git clone https://github.com/evalplus/evalplus.git
cd evalplus
```

### Step 2: Configure the Python Path

```bash
export PYTHONPATH=$PYTHONPATH:$(pwd)
```

### Step 3: Install Required Dependencies (Data Access Only)

```bash
pip install -r requirements.txt
pip install -e .
```

> These steps are only required to enable access to EvalPlus’s data-loading interfaces and do **not** trigger any evaluation procedures.

### Step 4: Create the Mini Dataset Extraction Script

```bash
nano extract_mini.py
```

Add the following content to `extract_mini.py`:

```python
import json
from pathlib import Path
from evalplus.data.humaneval import get_human_eval_plus, get_human_eval

"""
Construct a dataset with:
- HumanEvalPlus full task definitions
- Mini-selected input sets
- Original HumanEval test harness

No evaluation or execution is performed.
"""

# 1. Load datasets
plus_full = get_human_eval_plus(mini=False)
plus_mini = get_human_eval_plus(mini=True)
human_eval = get_human_eval()

# 2. Consistency checks
assert plus_full.keys() == plus_mini.keys(), "Mismatch between full and mini tasks"
assert plus_full.keys() == human_eval.keys(), "Mismatch with HumanEval tasks"

print("Number of tasks:", len(plus_full))

# 3. Merge datasets
out_path = Path(__file__).resolve().parent / "humanevalplus_full_mini_inputs_with_test.jsonl"
with open(out_path, "w") as f:
    for task_id in plus_full:
        full_task = plus_full[task_id]
        mini_task = plus_mini[task_id]
        he_task = human_eval[task_id]

        merged_task = {
            # identity
            "task_id": task_id,

            # from HumanEvalPlus (full)
            "prompt": full_task["prompt"],
            "contract": full_task.get("contract"),
            "entry_point": full_task["entry_point"],
            "canonical_solution": full_task["canonical_solution"],

            # mini-selected inputs
            "base_input": mini_task["base_input"],
            "plus_input": mini_task["plus_input"],
            "atol": mini_task.get("atol"),

            # from original HumanEval
            "test": he_task["test"],
        }

        f.write(json.dumps(merged_task) + "\n")

print(f"Dataset written to {out_path}")
```

Save and exit.

### Step 5: Run the Script and Generate the Dataset File

```bash
python extract_mini.py
```

Upon successful execution, the following file will be generated:

```text
humanevalplus_full_mini_inputs_with_test.jsonl
```

This file corresponds to the **HumanEvalPlus-Mini dataset**, containing the original HumanEval tasks together with the mini-selected EvalPlus test inputs, and does not include any model outputs or evaluation results.

### Step 6: Move the Generated Dataset File

After the dataset file has been successfully generated, move it to the parent directory for easier access by downstream scripts.
```bash
mv humanevalplus_full_mini_inputs_with_test.jsonl ..
```

After this step, the file will be located at:
```text
../humanevalplus_full_mini_inputs_with_test.jsonl
```