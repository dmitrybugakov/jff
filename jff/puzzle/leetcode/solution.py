from heapq import merge
from typing import List, Any


def remove_duplicates(nums: List[int]) -> int:
    i = 0
    while i < len(nums) - 1:
        if nums[i] == nums[i + 1]:
            del nums[i]
        else:
            i += 1
    return len(nums)


def is_palindrome(x: int) -> bool:
    return str(x) == str(x)[::-1]


def median_of_two_sorted_arrays(x: List[int], y: List[int]) -> float:
    merged = list(merge(x, y))
    length = len(merged)
    middle = length >> 1

    print(length)
    print(middle)

    if length % 2 == 1:
        return merged[middle]
    else:
        return (merged[middle - 1] + merged[middle]) / 2


def get_no_zero_integers(n: int) -> List[int]:
    """returns the converted integer into the sum of two no-zero integers"""

    def get_sum(minuend: int, deductible: int) -> List[int]:
        if '0' in str(minuend) or '0' in str(deductible):
            return get_sum(minuend - 1, deductible + 1)
        else:
            return [minuend, deductible]

    return get_sum(n - 1, 1)


def minimum_flips(a: int, b: int, c: int) -> int:
    """returns the minimum flips to make a or b equal to c"""
    print("a:{0} is {0:b}".format(a))
    print("b:{0} is {0:b}".format(b))
    print("c:{0} is {0:b}".format(c))

    print("{0:b}".format((a ^ b)))

    return 0
