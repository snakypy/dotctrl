from os import remove, symlink
from os.path import join
from shutil import copyfile

from snakypy.dotctrl.actions.link import LinkCommand
from snakypy.dotctrl.utils import is_repo_symbolic_link

from .test_init import InitTester
from .test_pull import PullTester
from .utilities import Basic, fixture  # noqa: E261,F401


class LinkTester(Basic):
    def __init__(self, fixt):  # noqa: F811
        Basic.__init__(self, fixt)

    @property
    def link(self):
        return self.menu.args(argv=["link"])

    def __element(self, elem):
        return self.menu.args(argv=["link", f"--e={elem}"])

    def __element_force(self, elem):
        return self.menu.args(argv=["link", f"--e={elem}", "--f"])

    def massive(self):

        output = LinkCommand(self.root, self.home).main(self.link)

        assert output["status"] is True

        for e in self.elements:
            elem_home = join(self.home, e)
            elem_repo = join(self.base.repo_path, e)

            assert is_repo_symbolic_link(elem_home, elem_repo) is True

        assert output["code"] == "15"

    def specific_element(self, elem):

        output = LinkCommand(self.root, self.home).main(self.__element(elem))

        assert output["status"] is True

        elem_home = join(self.home, elem)
        elem_repo = join(self.base.repo_path, elem)

        assert is_repo_symbolic_link(elem_home, elem_repo) is True

        # # Checking for error if there are two elements with the same name in
        # # the source and destination location.
        remove(elem_home)

        # Copy file repo to origin
        copyfile(elem_repo, elem_home)

        output = LinkCommand(self.root, self.home).main(self.__element(elem))

        assert output["code"] == "27"

        # # Creating intrusive symbolic link to force an error.
        remove(elem_home)

        symlink(join(self.home, "foo.txt"), join(self.home, elem))

        output = LinkCommand(self.root, self.home).main(self.__element(elem))

        assert output["code"] == "39"

        # # # Using option --force (--f)
        output = LinkCommand(self.root, self.home).main(self.__element_force(elem))

        assert is_repo_symbolic_link(elem_home, elem_repo) is True


def test_link_massive(fixture):  # noqa: F811
    InitTester(fixture).run()
    PullTester(fixture).massive()
    link = LinkTester(fixture)
    link.massive()


def test_link_specific_element(fixture):  # noqa: F811
    link = LinkTester(fixture)
    InitTester(fixture).run()
    PullTester(fixture).specific_element(link.elements[0])
    link.specific_element(link.elements[0])
