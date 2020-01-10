import unittest

from jff.puzzle.leetcode import solution


class BasicTestSuite(unittest.TestCase):

    @staticmethod
    def test_remove_duplicates() -> object:
        assert solution.remove_duplicates([1, 2]) == 2, "Should be 2"

    @staticmethod
    def test_is_palindrome() -> object:
        assert solution.is_palindrome(101) == True, "Should be True"


if __name__ == '__main__':
    unittest.main()
