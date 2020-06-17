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
