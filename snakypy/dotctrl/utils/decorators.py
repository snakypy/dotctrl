from functools import wraps
from typing import Any


def assign_cli(arguments: Any, command: str):
    """Decorator to assign docopt command to a given function"""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if arguments[command]:
                return func(*args, **kwargs)

        return wrapper

    return decorator
