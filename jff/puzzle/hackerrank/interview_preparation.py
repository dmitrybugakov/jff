from collections import Counter
from typing import Dict, List


def make_anagram(a: str, b: str) -> int:
    """ returns an integer representing the minimum total characters
        that must be deleted to make the strings anagrams """
    count = 0
    for i in range(97, 123):
        ia = sum(letter == chr(i) for letter in a)
        ib = sum(letter == chr(i) for letter in b)
        count += abs(ia - ib)
    return count


def alternating_characters(letters: str) -> int:
    """ returns an integer representing the minimum number of
        deletions to make the alternating string """
    count: int = 0
    size: int = len(letters)

    for i in range(size - 1):
        if letters[i] == letters[i + 1]:
            count += 1

    return count


def is_valid(value: str) -> bool:
    """ The string to be valid if all characters of the string appear the same number of times.
    It is also valid if he can remove just  character at  index in the string, and the remaining
    characters will occur the same number of times. Given a string , determine if it is valid.
    If so, return true, otherwise return false. """
    counter: Counter = Counter(value)
    distribution: Dict = {}
    for key in counter:
        distribution[counter[key]] = distribution.get(counter[key], 0) + 1

    keys: List = list(distribution.keys())
    if len(keys) == 1:
        return True
    elif len(keys) == 2:
        key1 = keys.pop()
        key2 = keys.pop()
        if (((abs(key1 - key2) == 1) and distribution[max(key1, key2)] == 1) or
                ((abs(key1 - key2) >= 1) and distribution[min(key1, key2)] == 1)):
            return True

    return False


def substring_count(length: int, value: str) -> int:
    """
    A string is said to be a special string if either of two conditions is met:
    All of the characters are the same, e.g. aaa.
    All characters except the middle one are the same, e.g. aadaa.
    return an integer representing the number of special substrings that can be formed from the given string.
    """
    result: int = 0

    for step in range(2, length + 1):
        left_border: int = 0
        right_border: int = step - 1

        while right_border < length:
            i = left_border
            j = right_border
            middle: int = left_border + right_border >> 1

            if step % 2 == 1:
                while (i < j) and ((i + 1 == middle and value[i] == value[i + 2]) or (value[i] == value[i + 1])):
                    if i + 1 == middle:
                        i += 2
                    else:
                        i += 1
            else:
                while i < j and value[i] == value[i + 1]:
                    i += 1

            if i == j:
                result += 1

            left_border += 1
            right_border += 1

    return length + result
