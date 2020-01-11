import unittest

from jff.tricks.decorator import power


class BasicTestSuite(unittest.TestCase):

    @staticmethod
    def test_decorator_power() -> None:
        @power(2)
        def rise(n: int) -> int:
            return n

        result: int = 100
        assert rise(10) == result, "Should be {0}".format(result)


if __name__ == '__main__':
    unittest.main()
