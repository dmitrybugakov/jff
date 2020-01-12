import unittest
from typing import Any

from jff.puzzle.hackerrank import solution


class BasicTestSuite(unittest.TestCase):
    @classmethod
    def setUpClass(cls: Any) -> None:
        cls.errorMessage = "Should be {0}"

    def test_make_anagram(self: Any) -> None:
        result: int = 0
        assert solution.make_anagram("abc", "abc") == 0, self.errorMessage.format(result)


if __name__ == '__main__':
    unittest.main()
