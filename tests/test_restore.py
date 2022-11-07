from os.path import exists, join

from snakypy.dotctrl.actions.restore import RestoreCommand

from .test_init import InitTester
from .test_link import LinkTester
from .test_pull import PullTester
from .utilities import Basic, fixture  # noqa: E261,F401

# from unittest.mock import patch


class RestoreTester(Basic):
    def __init__(self, fixt):  # noqa: F811
        Basic.__init__(self, fixt)
        self.fixt = fixt

    @property
    def restore(self):
        return self.menu.args(argv=["restore"])

    def __element(self, elem):
        return self.menu.args(argv=["restore", f"--e={elem}"])

    # @patch("builtins.input", lambda _: "1")
    def massive(self, monkeypatch, replay):
        """Using dialog"""

        # Pytest has a new monkeypatch fixture for this. A monkeypatch object
        # can alter an attribute in a class or a value in a dictionary, and
        # then restore its original value at the end of the test.
        monkeypatch.setattr("builtins.input", lambda _: replay)

        if replay == "1":
            output = RestoreCommand(self.root, self.home).main(self.restore)

            assert output["code"] == "40"

            PullTester(self.fixt).massive()
            LinkTester(self.fixt).massive()

            output = RestoreCommand(self.root, self.home).main(self.restore)

            for e in self.elements:
                assert exists(join(self.base.repo_path, e)) is False

            assert output["code"] == "46"

            output = RestoreCommand(self.root, self.home).main(self.restore)

            assert output["code"] == "38"

        elif replay == "2":

            PullTester(self.fixt).massive()
            LinkTester(self.fixt).massive()

            output = RestoreCommand(self.root, self.home).main(self.restore)

            assert output["code"] == "42"

    def specific_element(self, elem):

        output = RestoreCommand(self.root, self.home).main(
            self.__element(elem)
        )

        assert output["code"] == "46"

        output = RestoreCommand(self.root, self.home).main(
            self.__element(elem)
        )

        assert output["code"] == "38"


def test_restore_massive(fixture, monkeypatch):  # noqa: F811
    InitTester(fixture).run()
    restore = RestoreTester(fixture)
    restore.massive(monkeypatch, "1")
    restore.massive(monkeypatch, "2")


def test_restore_specific_element(fixture):  # noqa: F811
    restore = RestoreTester(fixture)
    InitTester(fixture).run()
    PullTester(fixture).specific_element(restore.elements[0])
    LinkTester(fixture).specific_element(restore.elements[0])
    restore.specific_element(restore.elements[0])
