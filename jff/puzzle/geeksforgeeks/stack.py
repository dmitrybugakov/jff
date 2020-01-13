from typing import Any, List


class AnyStack:
    def __init__(self: Any, init_state: List[Any] = None) -> None:
        """ initializes a stack object """
        if init_state is None:
            init_state = []
        self.__container = init_state

    def __get_container__(self: Any) -> List[Any]:
        return self.__container


class Stack(AnyStack):

    def push(self: Any, item: Any) -> None:
        """ add element into the head """
        self.__get_container__().append(item)

    def pop(self: Any) -> Any:
        """ returns the first element of the stack and drops it """
        return self.__get_container__().pop()

    def peek(self: Any) -> Any:
        """ returns the first element of the stack """
        if self.__get_container__:
            return self.__get_container__()[-1]
        else:
            raise Exception("Stack empty!")

    def is_empty(self: Any) -> bool:
        """ initializes a stack object """
        return self.size() == 0

    def size(self: Any) -> int:
        """ returns the size of the stack """
        return len(self.__get_container__())

    def show(self: Any) -> None:
        """ prints the stack """
        print(self.__get_container__())

    # def __eq__(self: Any, other: AnyStack) -> bool:
    #     """Overrides the default implementation"""
    #     return self.__get_container__() == other.__get_container__()
    #
    # def __ne__(self: Any, other: AnyStack) -> bool:
    #     """Overrides the default implementation (unnecessary in Python 3)"""
    #     return not self.__eq__(other)
