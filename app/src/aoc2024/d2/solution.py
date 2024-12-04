def main() -> None:
    reports = read_input_file()
    unsafe_reports = list(filter(lambda x: not determine_report_safe(x), reports))

    print(f"There are {len(reports) - len(unsafe_reports)} safe reports")

    safe_reports_after_dampening = list(
        filter(determine_safe_after_dampening, unsafe_reports)
    )

    print(
        f"There are {len(safe_reports_after_dampening)} that are now safe after dampening"
    )
    print(
        f"There are {len(reports) - len(unsafe_reports) + len(safe_reports_after_dampening)} total safe reports now"
    )


def read_input_file() -> list[list[int]]:
    with open("./input.txt") as input_file:
        input_rows = input_file.readlines()
        input_rows = [x.strip() for x in input_rows]
    report_list = []
    for row in input_rows:
        report_list.append([int(x) for x in row.split()])

    return report_list


def determine_report_safe(report: list[int]) -> bool:
    # Determine if the list should be increasing or decreasing
    if report[0] > report[1]:
        should_increase = False
    else:
        should_increase = True

    for a, b in zip(report, report[1:]):
        if (should_increase and b < a) or (not should_increase and b > a):
            return False
        if abs(a - b) > 3 or abs(a - b) < 1:
            return False
    return True


def determine_safe_after_dampening(unsafe_report: list[int]) -> bool:
    for index, _ in enumerate(unsafe_report):
        # Attempt to remove the element at the index. If the report is now safe, then
        # return True
        if determine_report_safe(unsafe_report[:index] + unsafe_report[index + 1 :]):
            return True

    return False


if __name__ == "__main__":
    main()
