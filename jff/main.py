from typing import List

from jff.algorithms.stanford import multiplication, karatsuba, merge_sort


def main() -> None:
    # print(multiplication(x="1234", y="2341", n=4))
    # print(karatsuba(x="1234", y="2341", n=4))
    print(merge_sort([1, 2, 3, 4, 6, 5]))


if __name__ == "__main__":
    main()
