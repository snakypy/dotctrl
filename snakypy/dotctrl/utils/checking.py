from os.path import realpath
from functools import reduce
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
    data = reduce(lambda c, k: c.get(k, {}), args, dictionary)
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


# # DEPRECATED
# def check_init(root) -> None:
#     """Function that ends commands that depend on the created repository, but
#     the repository was not created."""
#     if not exists(join(root, __info__["config"])):
#         printer(
#             f"The repository was not created. "
#             f"Use \"{__info__['pkg_name']} init [--auto | --git]\". Aborted",
#             foreground=FG().WARNING,
#         )
#         exit(1)
