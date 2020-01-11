from typing import Any


def power(exponent: int):
    def decorator(f: Any):
        def inner(*args: Any):
            result = f(*args)
            return result ** exponent

        return inner

    return decorator
