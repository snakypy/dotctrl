import locale
from os.path import realpath


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


def is_repo_symbolic_link(pathlink: str, repopath: str) -> bool:
    if realpath(pathlink) == repopath:
        return True
    return False


def lang_sys(languages: dict) -> str:
    """Get the language of the operating system."""

    lang = locale.getdefaultlocale()[0]

    if lang in languages:
        return lang

    return "en_US"
