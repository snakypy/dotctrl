from os import symlink, remove
from .utilities import base  # noqa: E261,F401
from .test_link import link_massive
from snakypy.dotctrl.utils.decorators import assign_cli
from snakypy.dotctrl.actions.repo import RepoCommand
from os.path import join


def repo_check(base):  # noqa: F811
    args = base["Menu"].args(argv=["repo", "--check"])

    @assign_cli(args, "repo")
    def wrapper():
        link_massive(base)

        out = RepoCommand(base["root"], base["home"]).main(args)

        if out["code"] != "21":
            assert False

        remove(join(base["home"], base["elements"][0]))
        intruder = join(base["home"], "intruder.txt")
        symlink(intruder, join(base["home"], base["elements"][0]))

        out = RepoCommand(base["root"], base["home"]).main(args)

        if out["code"] != "22":
            assert False

    return wrapper()


def test_repo_check(base):  # noqa: F811
    repo_check(base)
