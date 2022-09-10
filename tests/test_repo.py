from os import symlink, remove
from .utilities import Basic, fixture  # noqa: E261,F401
from .test_pull import PullTester
from .test_init import InitTester
from .test_link import LinkTester
from snakypy.dotctrl.utils.decorators import assign_cli
from snakypy.dotctrl.actions.repo import RepoCommand
from os.path import join


class RepoTester(Basic):
    def __init__(self, fixt):  # noqa: F811
        Basic.__init__(self, fixt)

    def opt(self, option):
        return self.menu.args(argv=["repo", option])

    def check(self):
        @assign_cli(self.opt("--check"), "repo")
        def wrapper():

            output = RepoCommand(self.root, self.home).main(self.opt("--check"))

            if output["code"] != "21":
                assert False

            remove(join(self.home, self.elements[0]))

            symlink(join(self.home, "foo.txt"), join(self.home, self.elements[0]))

            out = RepoCommand(self.root, self.home).main(self.opt("--check"))

            if out["code"] != "22":
                assert False

        return wrapper()


def test_repo_check(fixture):  # noqa: F811
    InitTester(fixture).run()
    PullTester(fixture).massive()
    LinkTester(fixture).massive()
    repo = RepoTester(fixture)
    repo.check()
