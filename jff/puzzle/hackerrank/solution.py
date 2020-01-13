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
