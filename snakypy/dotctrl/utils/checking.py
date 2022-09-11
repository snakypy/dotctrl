from functools import reduce
from os.path import realpath
from typing import Union


def is_repo_symbolic_link(pathlink: str, repopath: str) -> bool:
    if realpath(pathlink) == repopath:
        return True

    return False


def get_key(dictionary: dict, *args) -> Union[str, bool, dict]:
    """
    Function to get keys from a dictionary recursively without errors.
    If the key does not exist it returns an empty dictionary.
    Args:
        dictionary ([dict]): Receive a dictionary
    Returns:
        [str, bool]: Returning a str or a boolean if the object is True or False.
    """
    data: dict = reduce(lambda c, k: c.get(k, {}), args, dictionary)
    if data == {}:
        return ""

    return data


# # NOT USED
# def lang_sys(languages: dict) -> str:
#     import locale

#     """Get the language of the operating system."""

#     lang = locale.getdefaultlocale()[0]

#     if lang in languages:
#         return lang

#     return "en_US"
