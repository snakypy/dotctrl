from .utilities import Basic, fixture  # noqa: E261,F401
from .test_init import InitTester
from .test_pull import PullTester
from .test_link import LinkTester
from snakypy.dotctrl.actions.restore import RestoreCommand
from os.path import exists, join

# from unittest.mock import patch


class RestoreTester(Basic):
    def __init__(self, fixt):  # noqa: F811
        Basic.__init__(self, fixt)

    @property
    def restore(self):
        return self.menu.args(argv=["restore"])

    def __element(self, elem):
        return self.menu.args(argv=["restore", f"--e={elem}"])

    # @patch("builtins.input", lambda _: "1")
    def massive(self, monkeypatch, replay):

        # Pytest has a new monkeypatch fixture for this. A monkeypatch object can alter
        # an attribute in a class or a value in a dictionary, and then restore its
        # original value at the end of the test.
        monkeypatch.setattr("builtins.input", lambda _: replay)

        output = RestoreCommand(self.root, self.home).main(self.restore)

        if replay == "1":

            for e in self.elements:
                if exists(join(self.base.repo_path, e)):
                    assert False

            if output["code"] != "46":
                assert False

            output = RestoreCommand(self.root, self.home).main(self.restore)

            if output["code"] != "38":
                assert False

        elif replay == "2":

            if output["code"] != "42":
                assert False

    def specific_element(self, elem):

        output = RestoreCommand(self.root, self.home).main(self.__element(elem))

        if output["code"] != "46":
            assert False

        output = RestoreCommand(self.root, self.home).main(self.__element(elem))

        if output["code"] != "38":
            assert False


def test_restore_massive(fixture, monkeypatch):  # noqa: F811
    InitTester(fixture).run()
    PullTester(fixture).massive()
    LinkTester(fixture).massive()
    restore = RestoreTester(fixture)
    restore.massive(monkeypatch, "1")
    restore.massive(monkeypatch, "2")


def test_restore_specific_element(fixture):  # noqa: F811
    restore = RestoreTester(fixture)
    InitTester(fixture).run()
    PullTester(fixture).specific_element(restore.elements[0])
    LinkTester(fixture).specific_element(restore.elements[0])
    restore.specific_element(restore.elements[0])
