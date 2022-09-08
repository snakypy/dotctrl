from .utilities import base  # noqa: E261,F401
from .utilities import add_elements
from .test_init import test_init
from snakypy.dotctrl.actions.pull import PullCommand
from snakypy.dotctrl.utils.decorators import assign_cli
from os.path import exists, join
from shutil import copyfile


def pull_massive(base):  # noqa: F811
    args = base["Menu"].arguments(argv=["pull"])

    @assign_cli(args, "pull")
    def wrapper():
        test_init(base)
        add_elements(base, *base["elements"])

        PullCommand(base["root"], base["home"]).main(args)

        for e in base["elements"]:
            repo_path = base["Base"].repo_path
            if not exists(join(repo_path, e)):
                assert False

    return wrapper()


def pull_element(base):  # noqa: F811
    args = base["Menu"].arguments(argv=["pull", f"--e={base['elements'][0]}"])

    @assign_cli(args, "pull")
    def wrapper():
        test_init(base)
        add_elements(base, *base["elements"])

        out = PullCommand(base["root"], base["home"]).main(args)

        repo_path = base["Base"].repo_path
        if not exists(join(repo_path, base["elements"][0])):
            assert False

        if out["code"] != "18":
            assert False

        out = PullCommand(base["root"], base["home"]).main(args)

        if out["code"] != "16":
            assert False

        intruder = join(base["home"], "intruder.txt")

        copyfile(intruder, join(base["home"], base["elements"][0]))

        out = PullCommand(base["root"], base["home"]).main(args)

        if out["code"] != "37":
            assert False

    return wrapper()


def test_pull_massive(base):  # noqa: F811
    pull_massive(base)


def test_pull_element(base):  # noqa: F811
    pull_element(base)
