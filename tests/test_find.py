from snakypy.dotctrl.actions.find import FindCommand

from .test_init import InitTester
from .test_pull import PullTester
from .utilities import Basic, fixture  # noqa: E261,F401


class FindTester(Basic):
    def __init__(self, fixt):
        Basic.__init__(self, fixt)
        self.fixt = fixt

    def find(self, elem):
        return self.menu.args(argv=["find", f"--name={elem}"])

    def run(self, elem):

        output = FindCommand(self.root, self.home).main(self.find(elem))

        assert output["code"] == "28"

        InitTester(self.fixt).run()

        output = FindCommand(self.root, self.home).main(self.find(elem))

        assert output["code"] == "02"

        PullTester(self.fixt).massive()

        output = FindCommand(self.root, self.home).main(self.find(elem))

        assert output["code"] == "03"

        output = FindCommand(self.root, self.home).main(
            self.find("notexists.txt")
        )

        assert output["code"] == "04"


def test_find(fixture):  # noqa: F811
    find = FindTester(fixture)
    find.run(find.elements[0])
