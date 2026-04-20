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

# load HumanEvalPlus-Mini
dataset = get_human_eval_plus(mini=True)

print("Number of tasks:", len(dataset))

first_task = next(iter(dataset.values()))
print("Keys per task:", first_task.keys())

# export to jsonl
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

### Step 6: Move the Generated Dataset File

After the dataset file has been successfully generated, move it to the parent directory for easier access by downstream scripts.

```bash
mv humanevalplus_mini.jsonl ..
```


After this step, the file will be located at:

```text
../humanevalplus_mini.jsonl
```