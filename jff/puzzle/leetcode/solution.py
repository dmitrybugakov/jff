from heapq import merge
from typing import List


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
