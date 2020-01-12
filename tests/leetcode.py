import unittest
from typing import List, Any

from jff.puzzle.leetcode import solution


class BasicTestSuite(unittest.TestCase):
    @classmethod
    def setUpClass(cls: Any) -> None:
        cls.errorMessage = "Should be {0}"

    def test_remove_duplicates(self: Any) -> None:
        result: int = 2
        assert solution.remove_duplicates([1, 2]) == result, self.errorMessage.format(result)

    def test_is_palindrome(self: Any) -> None:
        result: bool = True
        assert solution.is_palindrome(101) is True, self.errorMessage.format(result)

    def test_median_of_two_sorted_arrays(self: Any) -> None:
        result: int = 2
        assert solution.median_of_two_sorted_arrays([1, 2], [3]) == 2, self.errorMessage.format(result)

    def test_get_no_zero_integers(self: Any) -> None:
        result: List[int] = [1, 1]
        assert solution.get_no_zero_integers(2) == result, self.errorMessage.format(result)


if __name__ == '__main__':
    unittest.main()
