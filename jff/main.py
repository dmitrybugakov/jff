from jff.puzzle.hackerrank.interview_preparation import substring_count


def main() -> None:
    length: int = 5
    value: str = "aabaa"
    result = substring_count(length=length, value=value)
    print(result)


if __name__ == "__main__":
    main()
