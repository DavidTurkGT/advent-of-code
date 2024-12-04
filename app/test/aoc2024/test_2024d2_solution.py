from src.aoc2024.d2.solution import determine_report_safe


def test_determine_report_safe():
    report_1 = [7, 6, 4, 2, 1]
    report_2 = [1, 2, 7, 8, 9]
    report_3 = [9, 7, 6, 2, 1]
    report_4 = [1, 3, 2, 4, 5]
    report_5 = [8, 6, 4, 4, 1]
    report_6 = [1, 3, 6, 7, 9]
    report_7 = [6, 4, 7, 8, 10, 11]

    assert determine_report_safe(report_1) is True
    assert determine_report_safe(report_2) is False
    assert determine_report_safe(report_3) is False
    assert determine_report_safe(report_4) is False
    assert determine_report_safe(report_5) is False
    assert determine_report_safe(report_6) is True
    assert determine_report_safe(report_7) is False
