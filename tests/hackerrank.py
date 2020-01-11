import unittest

from jff.puzzle.hackerrank import solution


class BasicTestSuite(unittest.TestCase):

    @staticmethod
    def test_make_anagram() -> None:
        result: int = 0
        assert solution.make_anagram("", "") == 0, "Should be {0}".format(result)


if __name__ == '__main__':
    unittest.main()
