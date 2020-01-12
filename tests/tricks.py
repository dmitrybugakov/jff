import unittest
from typing import Any, Tuple

from jff.tricks.decorator import power


class BasicTestSuite(unittest.TestCase):
    @classmethod
    def setUpClass(cls: Any) -> None:
        cls.errorMessage = "Should be {0}"

    def test_decorator_power(self: Any) -> None:
        @power(2)
        def rise(n: int) -> int:
            return n

        result: int = 100
        assert rise(10) == result, self.errorMessage.format(result)

    def test_swap_without_tmp(self: Any) -> None:
        def swap(a: int, b: int) -> Tuple[int, int]:
            a ^= b
            b ^= a
            a ^= b
            return a, b

        result: Tuple[int, int] = (3, 2)
        assert swap(2, 3) == result, self.errorMessage.format(result)


if __name__ == '__main__':
    unittest.main()
