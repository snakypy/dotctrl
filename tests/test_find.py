from .utilities import Basic, fixture  # noqa: E261,F401
from .test_init import InitTester
from .test_pull import PullTester
from snakypy.dotctrl.actions.find import FindCommand


class FindTester(Basic):
    def __init__(self, fixt):
        Basic.__init__(self, fixt)
        self.fixt = fixt

    def find(self, elem):
        return self.menu.args(argv=["find", f"--name={elem}"])

    def run(self, elem):

        output = FindCommand(self.root, self.home).main(self.find(elem))

        if output["code"] != "28":
            assert False

        InitTester(self.fixt).run()

        output = FindCommand(self.root, self.home).main(self.find(elem))

        if output["code"] != "02":
            assert False

        PullTester(self.fixt).massive()

        output = FindCommand(self.root, self.home).main(self.find(elem))

        if output["code"] != "03":
            assert False

        output = FindCommand(self.root, self.home).main(self.find("notexists.txt"))

        if output["code"] != "04":
            assert False


def test_find(fixture):  # noqa: F811
    find = FindTester(fixture)
    find.run(find.elements[0])
