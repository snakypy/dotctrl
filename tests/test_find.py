from .utilities import Basic, fixture  # noqa: E261,F401
from .test_init import InitTester
from .test_pull import PullTester
from snakypy.dotctrl.utils.decorators import assign_cli
from snakypy.dotctrl.actions.find import FindCommand


class FindTester(Basic):
    def __init__(self, fixt):
        Basic.__init__(self, fixt)

    def find(self, elem):
        return self.menu.args(argv=["find", f"--name={elem}"])

    def run(self, elem):
        @assign_cli(self.find(elem), "find")
        def wrapper():
            output = FindCommand(self.root, self.home).main(self.find(elem))

            if output["code"] != "03":
                assert False

            output = FindCommand(self.root, self.home).main(self.find("notexists.txt"))

            if output["code"] != "04":
                assert False

        return wrapper()


def test_find(fixture):  # noqa: F811
    InitTester(fixture).run()
    PullTester(fixture).massive()
    find = FindTester(fixture)
    find.run(find.elements[0])
