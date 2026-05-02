import os
import sys
from csv import reader

import matplotlib.pyplot as plt


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(BASE_DIR)
HUMAN_RESULTS_ROOT = os.path.join(PROJECT_ROOT, "human_results")
NUMBER_OF_SAMPLES = 164


def _results_csv_path():
    return os.path.join(HUMAN_RESULTS_ROOT, "results.csv")


def calculate_correctness(path):
    matrix = []
    with open(_results_csv_path(), "r", encoding="utf-8") as f:
        csv_reader = reader(f)
        for row in csv_reader:
            matrix.append(row)
    correctness = 0
    for i in range(1, NUMBER_OF_SAMPLES + 1):
        if "N/A" not in matrix[i][1]:
            correctness += float(matrix[i][1])
    return float(correctness / NUMBER_OF_SAMPLES)


def calculate_different_correctness_cases(path):
    matrix = []
    with open(_results_csv_path(), "r", encoding="utf-8") as f:
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

    return [count_correct, count_incorrect, count_partially_correct]


def get_incorrect_and_partial_ids(path):
    matrix = []
    with open(_results_csv_path(), "r", encoding="utf-8") as f:
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
    matrix = []
    with open(_results_csv_path(), "r", encoding="utf-8") as f:
        csv_reader = reader(f)
        for row in csv_reader:
            matrix.append(row)

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
    matrix = []
    with open(_results_csv_path(), "r", encoding="utf-8") as f:
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
        with open(os.path.join(HUMAN_RESULTS_ROOT, str(i), "output_validity.txt"), "r", encoding="utf-8") as f:
            content = f.read().splitlines()
            results.append(content[0])
    return results


def count_invalid(path):
    matrix = []
    with open(_results_csv_path(), "r", encoding="utf-8") as f:
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
    matrix = []
    with open(_results_csv_path(), "r", encoding="utf-8") as f:
        csv_reader = reader(f)
        for row in csv_reader:
            matrix.append(row)

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
                    not_passed_ids.append(int(row[0]))
            except (ValueError, TypeError):
                pass
        results[metric_name] = (len(not_passed_ids), not_passed_ids)
    return results


def plot_correctness_bar_charts(path):
    case_counts = calculate_different_correctness_cases(path)
    matrix = []
    with open(_results_csv_path(), "r", encoding="utf-8") as f:
        csv_reader = reader(f)
        for row in csv_reader:
            matrix.append(row)

    case_labels = ["Correct", "Incorrect", "Partially Correct"]
    total_cases = sum(case_counts)
    case_legend_labels = [
        f"{label} = {(count / total_cases * 100):.1f}%" if total_cases else f"{label} = 0.0%"
        for label, count in zip(case_labels, case_counts)
    ]

    partial_ids = []
    partial_correctness_rates = []
    for i in range(1, NUMBER_OF_SAMPLES + 1):
        row = matrix[i]
        score = row[1]
        if 'N/A' in score:
            continue
        score_value = float(score)
        if 0 < score_value < 0.95:
            try:
                case_id = int(row[0])
            except (ValueError, TypeError):
                case_id = i - 1
            partial_ids.append(str(case_id))
            partial_correctness_rates.append(score_value * 100)

    fig1, ax1 = plt.subplots(figsize=(7, 5))
    wedges, _ = ax1.pie(case_counts, labels=None, autopct=None,
                        startangle=90, pctdistance=0.7, textprops={"fontsize": 9})
    ax1.set_title("Correctness Case Distribution")
    ax1.axis("equal")
    ax1.legend(wedges, case_legend_labels, loc="upper right",
               bbox_to_anchor=(1.35, 1.0), frameon=False, title="Cases")
    fig1.subplots_adjust(right=0.72)
    output_path_1 = os.path.join(
        HUMAN_RESULTS_ROOT, "plot_correctness_cases_pie.png")
    fig1.savefig(output_path_1, dpi=300, bbox_inches="tight")
    print(f"Saved chart to: {output_path_1}")

    fig2, ax2 = plt.subplots(figsize=(5, 4))
    ax2.bar(partial_ids, partial_correctness_rates)
    ax2.axhline(y=90, color='red', linestyle='--',
                linewidth=1, label='90% threshold')
    ax2.set_title("Partially Correct IDs vs Correctness")
    ax2.set_xlabel("Partially Correct ID")
    ax2.set_ylabel("Correctness Rate (%)")
    ax2.set_ylim(0, 100)
    ax2.legend()
    fig2.tight_layout(pad=1.5)
    output_path_2 = os.path.join(
        HUMAN_RESULTS_ROOT, "plot_correctness_percentage_bar.png")
    fig2.savefig(output_path_2, dpi=300, bbox_inches="tight")
    print(f"Saved chart to: {output_path_2}")

    plt.show()


if __name__ == "__main__":
    print()
    print("Average Correctness with Invalid Generations:",
          calculate_correctness(HUMAN_RESULTS_ROOT))
    print()
    different_correctness_cases = calculate_different_correctness_cases(
        HUMAN_RESULTS_ROOT)
    print("Correct:", str(different_correctness_cases[0]), "Incorrect:", str(
        different_correctness_cases[1]), "Partially Correct:", str(different_correctness_cases[2]))
    incorrect_ids, partially_correct_ids = get_incorrect_and_partial_ids(
        HUMAN_RESULTS_ROOT)
    print("Incorrect IDs:", ', '.join(str(i)
          for i in incorrect_ids) if incorrect_ids else 'None')
    print()
    correctness_by_percentage = calculate_correctness_by_percentage(
        HUMAN_RESULTS_ROOT)
    partial_ids_by_percentage = get_partial_ids_by_percentage(
        HUMAN_RESULTS_ROOT)
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
    print("Validity percentage:", calculate_validity(HUMAN_RESULTS_ROOT))
    print("Number of Invalid Generations:", count_invalid(HUMAN_RESULTS_ROOT))

    print("\nSonarQube Analysis (cases not passing criteria):")
    sonar_results = analyze_sonarqube_metrics(HUMAN_RESULTS_ROOT)
    for metric, (count, ids) in sonar_results.items():
        ids_str = ', '.join(str(i) for i in ids) if ids else 'None'
        print(f"{metric}: {count} cases not passed (IDs: {ids_str})")

    plot_correctness_bar_charts(HUMAN_RESULTS_ROOT)
