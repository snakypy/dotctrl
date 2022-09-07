from .utilities import base  # noqa: E261,F401
from .test_pull import pull_massive_not_force
from snakypy.dotctrl.actions.link import LinkCommand
from snakypy.dotctrl.utils.decorators import assign_cli
from os.path import join
from snakypy.dotctrl.utils import is_repo_symbolic_link
from shutil import copyfile
from os import remove, symlink


def link_massive_not_force(base):  # noqa: F811
    args = base["Menu"].arguments(argv=["link"])
    pull_massive_not_force(base)

    @assign_cli(args, "link")
    def wrapper():

        out = LinkCommand(base["root"], base["home"]).main(args)

        if not out["bool"]:
            assert False

        for e in base["elements"]:
            elem_home = join(base["home"], e)
            elem_repo = join(base["Base"].repo_path, e)

            if not is_repo_symbolic_link(elem_home, elem_repo):
                assert False

        if out["cod"] != "cod:15":
            assert False

        # Remove link
        remove(elem_home)

        # Copy file repo to origin
        copyfile(elem_repo, elem_home)

        out = LinkCommand(base["root"], base["home"]).main(args)

        if not out["cod"] == "cod:27":
            assert False

    return wrapper()


def link_element_not_force(base):  # noqa: F811
    args = base["Menu"].arguments(argv=["link", f"--e={base['elements'][0]}"])
    pull_massive_not_force(base)

    @assign_cli(args, "link")
    def wrapper():

        out = LinkCommand(base["root"], base["home"]).main(args)

        if not out["bool"]:
            assert False

        elem_home = join(base["home"], base["elements"][0])
        elem_repo = join(base["Base"].repo_path, base["elements"][0])

        if not is_repo_symbolic_link(elem_home, elem_repo):
            assert False

        # Remove link
        remove(elem_home)

        # Copy file repo to origin
        copyfile(elem_repo, elem_home)

        out = LinkCommand(base["root"], base["home"]).main(args)

        if not out["cod"] == "cod:27":
            assert False

        remove(elem_home)

        intruder = join(base["home"], "intruder.txt")

        symlink(intruder, join(base["home"], base["elements"][0]))

        out = LinkCommand(base["root"], base["home"]).main(args)

        if not out["cod"] == "cod:39":
            assert False

    return wrapper()


def test_link_massive_not_force(base):  # noqa: F811
    link_massive_not_force(base)


def test_link_element_not_force(base):  # noqa: F811
    link_element_not_force(base)
