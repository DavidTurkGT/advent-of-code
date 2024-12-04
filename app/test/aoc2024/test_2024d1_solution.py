from src.aoc2024.d1.solution import calculate_difference, calculate_similarity_score


def test_calculate_differences() -> None:
    left_list = [3, 4, 2, 1, 3, 3]
    right_list = [4, 3, 5, 3, 9, 3]

    difference = calculate_difference(left_list, right_list)
    assert difference == 11


def test_calculate_similarity_score():
    list_a = [3, 4, 2, 1, 3, 3]
    list_b = [4, 3, 5, 3, 9, 3]

    similarity_score = calculate_similarity_score(list_a, list_b)

    assert similarity_score == 31
