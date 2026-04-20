import os
from csv import reader
import matplotlib.pyplot as plt

NUMBER_OF_SAMPLES = 164


def calculate_correctness(path):
    # Read results CSV.
    matrix = []
    with open(path + "/results/results.csv", "r") as f:
        csv_reader = reader(f)
        for row in csv_reader:
            matrix.append(row)
    # Compute average correctness.
    correctness = 0
    for i in range(1, NUMBER_OF_SAMPLES + 1):
        if "N/A" not in matrix[i][1]:
            correctness += float(matrix[i][1])
    return float(correctness / NUMBER_OF_SAMPLES)


def calculate_different_correctness_cases(path):
    # Read results CSV.
    matrix = []
    with open(path + "/results/results.csv", "r") as f:
        csv_reader = reader(f)
        for row in csv_reader:
            matrix.append(row)

    count_correct = 0
    count_incorrect = 0
    count_partially_correct = 0

    for i in range(1, NUMBER_OF_SAMPLES + 1):
        if 'N/A' in matrix[i][1]:
            count_incorrect += 1
        else:
            if float(matrix[i][1]) >= 0.95:
                count_correct += 1
            elif float(matrix[i][1]) == 0.0:
                count_incorrect += 1
            else:
                count_partially_correct += 1

    results = [count_correct, count_incorrect, count_partially_correct]

    return results


def get_incorrect_and_partial_ids(path):
    # Read results CSV.
    matrix = []
    with open(path + "/results/results.csv", "r") as f:
        csv_reader = reader(f)
        for row in csv_reader:
            matrix.append(row)

    incorrect_ids = []
    partially_correct_ids = []

    for i in range(1, NUMBER_OF_SAMPLES + 1):
        row = matrix[i]
        score = row[1]
        try:
            case_id = int(row[0])
        except (ValueError, TypeError):
            case_id = i - 1

        if 'N/A' in score:
            incorrect_ids.append(case_id)
        else:
            score_value = float(score)
            if score_value == 0.0:
                incorrect_ids.append(case_id)
            elif score_value < 0.95:
                partially_correct_ids.append(case_id)

    return incorrect_ids, partially_correct_ids


def calculate_correctness_by_percentage(path):
    # Read results CSV.
    matrix = []
    with open(path + "/results/results.csv", "r") as f:
        csv_reader = reader(f)
        for row in csv_reader:
            matrix.append(row)

    # Count correctness ranges.
    count_75_95 = 0
    count_50_75 = 0
    count_25_50 = 0
    count_0_25 = 0
    for i in range(1, NUMBER_OF_SAMPLES + 1):
        if not 'N/A' in matrix[i][1]:
            if 0.95 > float(matrix[i][1]) > 0.75:
                count_75_95 += 1
            elif 0.75 >= float(matrix[i][1]) > 0.5:
                count_50_75 += 1
            elif 0.5 >= float(matrix[i][1]) > 0.25:
                count_25_50 += 1
            elif 0.25 >= float(matrix[i][1]) > 0:
                count_0_25 += 1
    return [count_75_95, count_50_75, count_25_50, count_0_25]


def get_partial_ids_by_percentage(path):
    # Read results CSV.
    matrix = []
    with open(path + "/results/results.csv", "r") as f:
        csv_reader = reader(f)
        for row in csv_reader:
            matrix.append(row)

    ids_75_95 = []
    ids_50_75 = []
    ids_25_50 = []
    ids_0_25 = []

    for i in range(1, NUMBER_OF_SAMPLES + 1):
        row = matrix[i]
        score = row[1]
        if 'N/A' in score:
            continue

        score_value = float(score)
        try:
            case_id = int(row[0])
        except (ValueError, TypeError):
            case_id = i - 1

        if 0.95 > score_value > 0.75:
            ids_75_95.append(case_id)
        elif 0.75 >= score_value > 0.5:
            ids_50_75.append(case_id)
        elif 0.5 >= score_value > 0.25:
            ids_25_50.append(case_id)
        elif 0.25 >= score_value > 0:
            ids_0_25.append(case_id)

    return [ids_75_95, ids_50_75, ids_25_50, ids_0_25]


def return_percentages_correctness(path):
    scores = calculate_correctness_by_percentage(path)
    scale_ratings = calculate_different_correctness_cases(path)

    percentages = []
    percentages_scale_ratings = []

    for i in range(len(scores)):
        percentages.append(float(scores[i] / sum(scores)))

    for i in range(len(scale_ratings)):
        percentages_scale_ratings.append(
            float(scale_ratings[i] / sum(scale_ratings)))

    return percentages, percentages_scale_ratings


def read_all_exec_results(path):
    results = []
    for i in range(0, NUMBER_OF_SAMPLES):
        with open(path + "/" + str(i) + "/output_correctness_validity.txt", "r") as f:
            content = f.read().splitlines()
            results.append(content[0])
    return results


def count_invalid(path):
    # Read results CSV.
    matrix = []
    with open(path + "/results/results.csv", "r") as f:
        csv_reader = reader(f)
        for row in csv_reader:
            matrix.append(row)
    count = 0
    for i in range(1, NUMBER_OF_SAMPLES + 1):
        if '0' in matrix[i][2]:
            count += 1
    return count


def calculate_validity(path):
    count = count_invalid(path)
    return float((NUMBER_OF_SAMPLES - count) / NUMBER_OF_SAMPLES)


def analyze_sonarqube_metrics(path):
    """Analyze SonarQube metrics and return failed case counts and IDs."""
    matrix = []
    with open(path + "/results/results.csv", "r") as f:
        csv_reader = reader(f)
        for row in csv_reader:
            matrix.append(row)

    # Metric name -> (column index, fail condition)
    metrics = {
        'security_rating': (3, lambda x: float(x) != 1.0),
        'bugs': (4, lambda x: int(float(x)) > 0),
        'code_smells': (5, lambda x: int(float(x)) > 0),
        'reliability_rating': (6, lambda x: float(x) != 1.0),
        'vulnerabilities': (7, lambda x: int(float(x)) > 0),
        'security_hotspots': (8, lambda x: int(float(x)) > 0),
        'maintainability_rating': (9, lambda x: float(x) != 1.0)
    }

    results = {}
    for metric_name, (col_idx, condition) in metrics.items():
        not_passed_ids = []
        for i in range(1, NUMBER_OF_SAMPLES + 1):
            row = matrix[i]
            val = row[col_idx]
            try:
                if condition(val):
                    # Case ID is in column 0.
                    not_passed_ids.append(int(row[0]))
            except (ValueError, TypeError):
                # Skip non-convertible values.
                pass
        results[metric_name] = (len(not_passed_ids), not_passed_ids)
    return results


def plot_correctness_bar_charts(path):
    case_counts = calculate_different_correctness_cases(path)
    percentage_counts = calculate_correctness_by_percentage(path)

    case_labels = ["Correct", "Incorrect", "Partially Correct"]
    percentage_labels = ["75-95", "50-75", "25-50", "0-25"]
    total_cases = sum(case_counts)
    case_legend_labels = [
        f"{label} = {(count / total_cases * 100):.1f}%" if total_cases else f"{label} = 0.0%"
        for label, count in zip(case_labels, case_counts)
    ]

    fig1, ax1 = plt.subplots(figsize=(7, 5))

    wedges, _ = ax1.pie(
        case_counts,
        labels=None,
        autopct=None,
        startangle=90,
        pctdistance=0.7,
        textprops={"fontsize": 9}
    )
    ax1.set_title("Correctness Case Distribution")
    ax1.axis("equal")
    ax1.legend(
        wedges,
        case_legend_labels,
        loc="upper right",
        bbox_to_anchor=(1.35, 1.0),
        frameon=False,
        title="Cases"
    )
    fig1.subplots_adjust(right=0.72)
    output_path_1 = os.path.join(
        path, "results", "plot_correctness_cases_pie.png")
    fig1.savefig(output_path_1, dpi=300, bbox_inches="tight")
    print(f"Saved chart to: {output_path_1}")

    fig2, ax2 = plt.subplots(figsize=(7, 5))
    ax2.bar(percentage_labels, percentage_counts)
    ax2.set_title("Correctness Percentage Distribution")
    ax2.set_ylabel("Count")
    fig2.tight_layout(pad=1.5)
    output_path_2 = os.path.join(
        path, "results", "plot_correctness_percentage_bar.png")
    fig2.savefig(output_path_2, dpi=300, bbox_inches="tight")
    print(f"Saved chart to: {output_path_2}")

    plt.show()


print()
print("Average Correctness with Invalid Generations:",
      calculate_correctness(os.getcwd()))
print()
different_correctness_cases = calculate_different_correctness_cases(
    os.getcwd())
print("Correct:", str(different_correctness_cases[0]), "Incorrect:", str(
    different_correctness_cases[1]), "Partially Correct:", str(different_correctness_cases[2]))
incorrect_ids, partially_correct_ids = get_incorrect_and_partial_ids(
    os.getcwd())
print("Incorrect IDs:", ', '.join(str(i)
      for i in incorrect_ids) if incorrect_ids else 'None')
print()
correctness_by_percentage = calculate_correctness_by_percentage(os.getcwd())
partial_ids_by_percentage = get_partial_ids_by_percentage(os.getcwd())
print("95 > N > 75:", correctness_by_percentage[0], "\n75 >= N > 50:", correctness_by_percentage[1],
      "\n50 >= N > 25:", correctness_by_percentage[2], "\n25 >= N > 0:", correctness_by_percentage[3])
print("95 > N > 75 IDs:", ', '.join(str(i)
      for i in partial_ids_by_percentage[0]) if partial_ids_by_percentage[0] else 'None')
print("75 >= N > 50 IDs:", ', '.join(str(i)
      for i in partial_ids_by_percentage[1]) if partial_ids_by_percentage[1] else 'None')
print("50 >= N > 25 IDs:", ', '.join(str(i)
      for i in partial_ids_by_percentage[2]) if partial_ids_by_percentage[2] else 'None')
print("25 >= N > 0 IDs:", ', '.join(str(i)
      for i in partial_ids_by_percentage[3]) if partial_ids_by_percentage[3] else 'None')
print()
print("Validity percentage:", calculate_validity(os.getcwd()))
print("Number of Invalid Generations:", count_invalid(os.getcwd()))

# SonarQube analysis summary.
print("\nSonarQube Analysis (cases not passing criteria):")
sonar_results = analyze_sonarqube_metrics(os.getcwd())
for metric, (count, ids) in sonar_results.items():
    ids_str = ', '.join(str(i) for i in ids) if ids else 'None'
    print(f"{metric}: {count} cases not passed (IDs: {ids_str})")

plot_correctness_bar_charts(os.getcwd())
