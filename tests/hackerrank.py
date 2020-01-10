import unittest

from jff.puzzle.hackerrank import solution


class BasicTestSuite(unittest.TestCase):

    @staticmethod
    def test_remove_duplicates() -> object:
        result: int = 0
        assert solution.make_anagram("", "") == 0, "Should be {}".format(result)


if __name__ == '__main__':
    unittest.main()
