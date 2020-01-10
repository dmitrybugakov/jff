from jff.puzzle import leetcode
from jff.puzzle import hackerrank


def main() -> object:
    result: float = leetcode.solution.median_of_two_sorted_arrays([1, 2], [3])
    print(result)


if __name__ == "__main__":
    main()
