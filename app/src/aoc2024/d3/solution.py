import re


def main():
    corrupted_memory = read_input_file()
    sum = calculate_sum_of_muls_from_corrupted_memory(corrupted_memory)

    print(f"The sum of all mul operations in the corrupted memory is {sum}")

    corrected_sum = calculate_sum_with_dos_and_donts(corrupted_memory)

    print(
        f"The corrected sum with do() and don't() taken into consideration is {corrected_sum}"
    )


def read_input_file() -> str:
    with open("./input.txt") as input_file:
        input_rows = input_file.read()
    return input_rows


def calculate_sum_of_muls_from_corrupted_memory(corrupted_memory_string: str) -> int:
    valid_mul_paramters = re.findall(r"mul\((\d+),(\d+)\)", corrupted_memory_string)
    return sum([int(x[0]) * int(x[1]) for x in valid_mul_paramters])


def calculate_sum_with_dos_and_donts(corrupted_memory_string: str) -> int:
    # Base case: if don't() is not in the string return total
    if "don't()" not in corrupted_memory_string:
        return calculate_sum_of_muls_from_corrupted_memory(corrupted_memory_string)

    # Find the first case of don't(), everything to the left should be counted
    i = corrupted_memory_string.find("don't()")
    total = calculate_sum_of_muls_from_corrupted_memory(corrupted_memory_string[:i])
    remaining_string = corrupted_memory_string[i:]

    # With everything to the right, find the first case of do() and recurse on the right hand side
    i = remaining_string.find("do()")
    return total + calculate_sum_with_dos_and_donts(remaining_string[i:])


if __name__ == "__main__":
    main()
