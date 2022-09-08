from .utilities import base  # noqa: E261,F401
from .test_pull import pull_massive
from snakypy.dotctrl.actions.link import LinkCommand
from snakypy.dotctrl.utils.decorators import assign_cli
from os.path import join
from snakypy.dotctrl.utils import is_repo_symbolic_link
from shutil import copyfile
from os import remove, symlink


def link_massive(base):  # noqa: F811
    args = base["Menu"].arguments(argv=["link"])
    args_f = base["Menu"].arguments(argv=["link", "--f"])

    pull_massive(base)

    @assign_cli(args, "link")
    def wrapper():

        out = LinkCommand(base["root"], base["home"]).main(args)

        if not out["status"]:
            assert False

        for e in base["elements"]:
            elem_home = join(base["home"], e)
            elem_repo = join(base["Base"].repo_path, e)

            if not is_repo_symbolic_link(elem_home, elem_repo):
                assert False

        if out["code"] != "15":
            assert False

        # # Checking for error if there are two elements with the same name in
        # # the source and destination location.
        remove(elem_home)

        copyfile(elem_repo, elem_home)

        out = LinkCommand(base["root"], base["home"]).main(args)

        if not out["code"] == "27":
            assert False

        # # Using option --force (--f)
        out = LinkCommand(base["root"], base["home"]).main(args_f)

        if not is_repo_symbolic_link(elem_home, elem_repo):
            assert False

    return wrapper()


def link_element(base):  # noqa: F811
    args = base["Menu"].arguments(argv=["link", f"--e={base['elements'][0]}"])
    args_f = base["Menu"].arguments(argv=["link", f"--e={base['elements'][0]}", "--f"])

    pull_massive(base)

    @assign_cli(args, "link")
    def wrapper():

        out = LinkCommand(base["root"], base["home"]).main(args)

        if not out["status"]:
            assert False

        elem_home = join(base["home"], base["elements"][0])
        elem_repo = join(base["Base"].repo_path, base["elements"][0])

        if not is_repo_symbolic_link(elem_home, elem_repo):
            assert False

        # # Checking for error if there are two elements with the same name in
        # # the source and destination location.
        remove(elem_home)

        # Copy file repo to origin
        copyfile(elem_repo, elem_home)

        out = LinkCommand(base["root"], base["home"]).main(args)

        if not out["code"] == "27":
            assert False

        # # Creating intrusive symbolic link to force an error.
        remove(elem_home)

        intruder = join(base["home"], "intruder.txt")

        symlink(intruder, join(base["home"], base["elements"][0]))

        out = LinkCommand(base["root"], base["home"]).main(args)

        if not out["code"] == "39":
            assert False

        # # Using option --force (--f)
        out = LinkCommand(base["root"], base["home"]).main(args_f)

        if not is_repo_symbolic_link(elem_home, elem_repo):
            assert False

    return wrapper()


def test_link_massive(base):  # noqa: F811
    link_massive(base)


def test_link_element(base):  # noqa: F811
    link_element(base)
