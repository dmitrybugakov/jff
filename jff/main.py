from typing import List

from jff.puzzle.leetcode.solution import build_an_array_with_stack_operations


def main() -> None:
    # target: List[int] = [1, 3]
    # n: int = 3
    # target: List[int] = [1, 2]
    # n: int = 4
    target: List[int] = [3, 4, 5, 6, 8, 9]
    n: int = 9
    print(build_an_array_with_stack_operations(target, n))

    expected: List[str] = ["Push", "Pop", "Push", "Pop", "Push", "Push", "Push", "Push", "Push", "Pop", "Push", "Push"]
    print(expected)


if __name__ == "__main__":
    main()
