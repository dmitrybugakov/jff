import copy
import unittest
from typing import Any, List

from jff.puzzle.geeksforgeeks.stack import Stack


class BasicTestSuite(unittest.TestCase):
    @classmethod
    def setUpClass(cls: Any) -> None:
        cls.stack = Stack()
        cls.errorMessage = "Should be {0}"

    def test_stack_size(self: Any) -> None:
        stack: Stack = copy.deepcopy(self.stack)
        result: int = 0
        assert stack.size() == result, self.errorMessage.format(result)

    def test_stack_push(self: Any) -> None:
        stack: Stack = copy.deepcopy(self.stack)
        stack.push(1)
        result: List[Any] = [1]
        assert stack.__get_container__() == result, self.errorMessage.format(result)

    def test_stack_pop(self: Any) -> None:
        stack: Stack = copy.deepcopy(self.stack)
        stack.push(1)
        result: int = 1
        assert stack.pop() == result, self.errorMessage.format(result)

    def test_stack_peek(self: Any) -> None:
        stack: Stack = copy.deepcopy(self.stack)
        stack.push(1)
        result: int = 1
        assert stack.peek() == result, self.errorMessage.format(result)

    def test_stack_is_empty(self: Any) -> None:
        stack: Stack = copy.deepcopy(self.stack)
        stack.push(1)
        result: bool = False
        assert stack.is_empty() == result, self.errorMessage.format(result)


if __name__ == '__main__':
    unittest.main()
