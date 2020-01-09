from typing import List

from jff.puzzle.leetcode import solution


def main() -> object:
    nums: List[int] = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    result: int = solution.remove_duplicates(nums)
    print(result)


if __name__ == "__main__":
    main()
