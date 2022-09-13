from os import remove, symlink
from os.path import join

from snakypy.dotctrl.actions.repo import RepoCommand

from .test_init import InitTester
from .test_link import LinkTester
from .test_pull import PullTester
from .utilities import Basic, fixture  # noqa: E261,F401


class RepoTester(Basic):
    def __init__(self, fixt):  # noqa: F811
        Basic.__init__(self, fixt)
        self.fixt = fixt

    def opt(self, option):
        return self.menu.args(argv=["repo", option])

    def check(self):

        output = RepoCommand(self.root, self.home).main(self.opt("--check"))

        assert output["code"] == "19"

        PullTester(self.fixt).massive()
        LinkTester(self.fixt).massive()

        output = RepoCommand(self.root, self.home).main(self.opt("--check"))

        assert output["code"] == "21"

        remove(join(self.home, self.elements[0]))

        symlink(join(self.home, "foo.txt"), join(self.home, self.elements[0]))

        out = RepoCommand(self.root, self.home).main(self.opt("--check"))

        assert out["code"] == "22"

    def ls(self):

        output = RepoCommand(self.root, self.home).main(self.opt("--ls"))

        assert output["code"] == "24"

        PullTester(self.fixt).massive()
        LinkTester(self.fixt).massive()

        out = RepoCommand(self.root, self.home).main(self.opt("--ls"))

        assert out["str"] == "success"


def test_repo_check(fixture):  # noqa: F811
    InitTester(fixture).run()
    repo = RepoTester(fixture)
    repo.check()


def test_repo_ls(fixture):  # noqa: F811
    InitTester(fixture).run()
    repo = RepoTester(fixture)
    repo.ls()
