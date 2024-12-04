def is_safe(report):
    differences = []
    for i in range(len(report) - 1):
        differences.append(report[i + 1] - report[i])

    for diff in differences:
        if not (1 <= abs(diff) <= 3):
            return False

    is_increasing = True
    is_decreasing = True

    for diff in differences:
        if diff <= 0:
            is_increasing = False
        if diff >= 0:
            is_decreasing = False

    if not (is_increasing or is_decreasing):
        return False

    return True


def main(file_path):
    reports = []
    with open(file_path, 'r') as file:
        for line in file:
            reports.append([int(num) for num in line.split()])

    safe_count = 0
    for report in reports:
        if is_safe(report):
            safe_count += 1

    return safe_count


if __name__ == "__main__":
    file_path = "E:\\Visual Studio Code\\Python\\Advent of Code - 2024\\Day 2\\Input.txt"
    safe_reports = main(file_path)
    print(f"Number of safe reports: {safe_reports}")
