import unittest

from jff.puzzle.leetcode import solution


class BasicTestSuite(unittest.TestCase):

    @staticmethod
    def test_remove_duplicates() -> object:
        result: int = 2
        assert solution.remove_duplicates([1, 2]) == result, "Should be {}".format(result)

    @staticmethod
    def test_is_palindrome() -> object:
        result: bool = True
        assert solution.is_palindrome(101) == True, "Should be {}".format(result)

    @staticmethod
    def test_median_of_two_sorted_arrays() -> object:
        result: int = 2
        assert solution.median_of_two_sorted_arrays([1, 2], [3]) == 2, "Should be {}".format(result)


if __name__ == '__main__':
    unittest.main()
