import unittest

from jff.puzzle.leetcode import solution


class BasicTestSuite(unittest.TestCase):

    @staticmethod
    def test_remove_duplicates() -> object:
        assert solution.remove_duplicates([1, 2]) == 2, "Should be 2"

    @staticmethod
    def test_is_palindrome() -> object:
        assert solution.is_palindrome(101) == True, "Should be True"

    @staticmethod
    def test_median_of_two_sorted_arrays() -> object:
        assert solution.median_of_two_sorted_arrays([1, 2], [3]) == 2, "Should be 2"


if __name__ == '__main__':
    unittest.main()
