def main() -> None:
    reports = read_input_file()
    safe_reports = list(filter(determine_report_safe, reports))

    print(f"There are {len(safe_reports)} safe reports")

    safe_reports_with_dampener = list(
        filter(lambda x: determine_report_safe(x, problem_dampener=True), reports)
    )
    print(f"There are {len(safe_reports_with_dampener)} safe reports after dampening")


def read_input_file() -> list[list[int]]:
    with open("./input.txt") as input_file:
        input_rows = input_file.readlines()
        input_rows = [x.strip() for x in input_rows]
    report_list = []
    for row in input_rows:
        report_list.append([int(x) for x in row.split()])

    return report_list


def determine_report_safe(
    levels: list[int], problem_dampener=False, rerun=False
) -> bool:
    if rerun:
        print(f"Looking at {levels}")
    # Determine if the list should be increasing or decreasing
    if levels[0] > levels[1]:
        should_increase = False
    else:
        should_increase = True

    for a, b in zip(levels, levels[1:]):
        if (should_increase and b < a) or (not should_increase and b > a):
            return False
        if abs(a - b) > 3 or abs(a - b) < 1:
            return False
    return True


if __name__ == "__main__":
    main()
