import re


def main():
    corrupted_memory = read_input_file()
    sum = calculate_sum_of_muls_from_corrupted_memory(corrupted_memory)

    print(f"The sum of all mul operations in the corrupted memory is {sum}")


def read_input_file() -> str:
    with open("./input.txt") as input_file:
        input_rows = input_file.readlines()
    return "".join(input_rows)


def calculate_sum_of_muls_from_corrupted_memory(corrupted_memory_string: str) -> int:
    valid_mul_paramters = re.findall(r"mul\((\d+),(\d+)\)", corrupted_memory_string)
    return sum([int(x[0]) * int(x[1]) for x in valid_mul_paramters])


if __name__ == "__main__":
    main()
