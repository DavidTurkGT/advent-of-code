def main() -> None:
    left_list, right_list = read_input_file()

    difference = calculate_difference(left_list, right_list)
    print(f"{difference=}")

    similarity_score = calculate_similarity_score(left_list, right_list)
    print(f"{similarity_score=}")


def read_input_file() -> tuple[list[int], list[int]]:
    with open("./input.txt") as input_file:
        input_rows = input_file.readlines()
        input_rows = [x.strip() for x in input_rows]
        input_rows = [x.split("   ") for x in input_rows]

    left_list = [int(e[0]) for e in input_rows]
    right_list = [int(e[1]) for e in input_rows]

    return left_list, right_list


def calculate_difference(list_a: list[int], list_b: list[int]) -> int:
    """
    Sorts each list then calculates the total absolute difference between
    elements of the lists with matching inputs
    """
    return sum(abs(a - b) for a, b in zip(sorted(list_a), sorted(list_b)))


def calculate_similarity_score(list_a: list[int], list_b: list[int]) -> int:
    similarity_score = 0

    for n in list_a:
        similarity_score += n * len(list(filter(lambda x, y=n,: x == y, list_b)))

    return similarity_score


if __name__ == "__main__":
    main()
