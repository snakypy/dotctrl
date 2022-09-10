from .utilities import Basic, fixture  # noqa: E261,F401
from .test_pull import PullTester
from .test_init import InitTester
from snakypy.dotctrl.actions.link import LinkCommand
from os.path import join
from snakypy.dotctrl.utils import is_repo_symbolic_link
from shutil import copyfile
from os import remove, symlink


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

        if not output["status"]:
            assert False

        for e in self.elements:
            elem_home = join(self.home, e)
            elem_repo = join(self.base.repo_path, e)

            if not is_repo_symbolic_link(elem_home, elem_repo):
                assert False

        if output["code"] != "15":
            assert False

    def specific_element(self, elem):

        output = LinkCommand(self.root, self.home).main(self.__element(elem))

        if not output["status"]:
            assert False

        elem_home = join(self.home, elem)
        elem_repo = join(self.base.repo_path, elem)

        if not is_repo_symbolic_link(elem_home, elem_repo):
            assert False

        # # Checking for error if there are two elements with the same name in
        # # the source and destination location.
        remove(elem_home)

        # Copy file repo to origin
        copyfile(elem_repo, elem_home)

        output = LinkCommand(self.root, self.home).main(self.__element(elem))

        if not output["code"] == "27":
            assert False

        # # Creating intrusive symbolic link to force an error.
        remove(elem_home)

        symlink(join(self.home, "foo.txt"), join(self.home, elem))

        output = LinkCommand(self.root, self.home).main(self.__element(elem))

        if not output["code"] == "39":
            assert False

        # # # Using option --force (--f)
        output = LinkCommand(self.root, self.home).main(self.__element_force(elem))

        if not is_repo_symbolic_link(elem_home, elem_repo):
            assert False


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
