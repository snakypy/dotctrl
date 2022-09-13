from os import remove, symlink
from os.path import join

from snakypy.dotctrl.actions.unlink import UnlinkCommand

from .test_init import InitTester
from .test_link import LinkTester
from .test_pull import PullTester
from .utilities import Basic, fixture  # noqa: E261,F401


class UnlinkTester(Basic):
    def __init__(self, fixt):  # noqa: F811
        Basic.__init__(self, fixt)
        self.fixt = fixt

    @property
    def unlink(self):
        return self.menu.args(argv=["unlink"])

    def __element(self, elem):
        return self.menu.args(argv=["unlink", f"--e={elem}"])

    def massive(self):

        output = UnlinkCommand(self.root, self.home).main(self.unlink)

        assert output["code"] == "31"

        output = UnlinkCommand(self.root, self.home).main(self.unlink)

        assert output["code"] == "30"

    def specific_element(self, elem):

        # Create a symbolic link from any file to generate an error.
        symlink(join(self.home, "foo.txt"), join(self.home, elem))

        output = UnlinkCommand(self.root, self.home).main(self.__element(elem))

        assert output["code"] == "39"

        # Remove the created link that was to generate the error
        remove(join(self.home, elem))

        LinkTester(self.fixt).specific_element(elem)

        output = UnlinkCommand(self.root, self.home).main(self.__element(elem))

        assert output["code"] == "12"

        output = UnlinkCommand(self.root, self.home).main(self.__element(elem))

        assert output["code"] == "29"


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
    unlink.specific_element(unlink.elements[0])
