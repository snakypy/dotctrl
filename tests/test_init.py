from os.path import exists

from snakypy.dotctrl.actions.init import InitCommand
from snakypy.dotctrl.actions.repo import RepoCommand

from .utilities import Basic, fixture  # noqa: E261, F401


class InitTester(Basic):
    def __init__(self, fixt):  # noqa: F811
        Basic.__init__(self, fixt)

    @property
    def args(self):
        return self.menu.args(argv=["init"])

    @property
    def repo_check(self):
        return self.menu.args(argv=["repo", "--check"])

    def run(self):

        output = RepoCommand(self.root, self.home).main(self.repo_check)

        assert output["code"] == "28"

        output = InitCommand(self.root, self.home).main(self.args)

        assert exists(self.base.config_path) is True

        assert exists(self.base.repo_path) is True

        assert output["code"] == "10"


def test_init(fixture):  # noqa: F811
    init = InitTester(fixture)
    init.run()
