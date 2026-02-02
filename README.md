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
from evalplus.data import get_human_eval_plus

# Load HumanEvalPlus-Mini (data only, no evaluation)
dataset = get_human_eval_plus(mini=True)

print("Number of tasks:", len(dataset))

# dataset is a dict: {task_id: task_dict}
first_task = next(iter(dataset.values()))
print("Keys per task:", first_task.keys())

# Export to a JSONL file
with open("humanevalplus_mini.jsonl", "w") as f:
    for task_id, task in dataset.items():
        f.write(json.dumps(task) + "\n")
```

Save and exit.

### Step 5: Run the Script and Generate the Dataset File

```bash
python extract_mini.py
```

Upon successful execution, the following file will be generated:

```text
humanevalplus_mini.jsonl
```

This file corresponds to the **HumanEvalPlus-Mini dataset**, containing the original HumanEval tasks together with the mini-selected EvalPlus test inputs, and does not include any model outputs or evaluation results.
