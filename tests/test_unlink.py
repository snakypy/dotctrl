from snakypy.dotctrl.actions.unlink import UnlinkCommand

from .test_init import InitTester
from .test_link import LinkTester
from .test_pull import PullTester
from .utilities import Basic, fixture  # noqa: E261,F401


class UnlinkTester(Basic):
    def __init__(self, fixt):  # noqa: F811
        Basic.__init__(self, fixt)

    @property
    def unlink(self):
        return self.menu.args(argv=["unlink"])

    def __element(self, elem):
        return self.menu.args(argv=["unlink", f"--e={elem}"])

    def massive(self):

        output = UnlinkCommand(self.root, self.home).main(self.unlink)

        if output["code"] != "31":
            assert False

        output = UnlinkCommand(self.root, self.home).main(self.unlink)

        if output["code"] != "30":
            assert False

    def specific_element(self, elem):

        output = UnlinkCommand(self.root, self.home).main(self.__element(elem))

        if output["code"] != "12":
            assert False

        output = UnlinkCommand(self.root, self.home).main(self.__element(elem))

        if output["code"] != "29":
            assert False


def test_unlink_massive(fixture):  # noqa: F811
    InitTester(fixture).run()
    PullTester(fixture).massive()
    LinkTester(fixture).massive()
    unlink = UnlinkTester(fixture)
    unlink.massive()


def test_unlink_specific_element(fixture):  # noqa: F811
    unlink = UnlinkTester(fixture)
    InitTester(fixture).run()
    PullTester(fixture).specific_element(unlink.elements[0])
    LinkTester(fixture).specific_element(unlink.elements[0])
    unlink.specific_element(unlink.elements[0])
