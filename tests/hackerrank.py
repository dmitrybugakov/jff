import unittest
from typing import Any

from jff.puzzle.hackerrank import solution


class BasicTestSuite(unittest.TestCase):
    @classmethod
    def setUpClass(cls: Any) -> None:
        cls.errorMessage = "Should be {0}"

    def test_make_anagram(self: Any) -> None:
        result: int = 0
        assert solution.make_anagram("abc", "abc") == result, self.errorMessage.format(result)

    def test_alternating_characters(self: Any) -> None:
        result: int = 8
        assert solution.alternating_characters("AAAABBBBCCC") == result, self.errorMessage.format(result)


if __name__ == '__main__':
    unittest.main()
