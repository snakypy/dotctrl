from functools import wraps


def assign_cli(arguments: callable(object), command: str):
    """Decorator to assign docopt command to a given function"""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if arguments[command]:
                return func(*args, **kwargs)

        return wrapper

    return decorator
