from src.aoc2024.d3.solution import (
    calculate_sum_of_muls_from_corrupted_memory,
    calculate_sum_with_dos_and_donts,
)


def test_calculate_sum_of_muls_from_corrupted_memory() -> None:
    corrupted_memory = (
        "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    )
    sum = calculate_sum_of_muls_from_corrupted_memory(corrupted_memory)
    assert sum == 161


def test_calculate_sum_with_dos_and_donts() -> None:
    corrupted_memory = (
        "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    )
    sum = calculate_sum_with_dos_and_donts(corrupted_memory)
    assert sum == 48
