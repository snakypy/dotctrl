from functools import wraps
from typing import Any


def assign_cli(arguments: Any, key: str):
    """Decorator to assign docopt key to a given function"""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if arguments[key]:
                return func(*args, **kwargs)

        return wrapper

    return decorator
