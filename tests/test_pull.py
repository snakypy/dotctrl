from .utilities import Basic, fixture  # noqa: E261,F401
from .test_init import InitTester
from snakypy.dotctrl.actions.pull import PullCommand
from snakypy.dotctrl.utils.decorators import assign_cli
from os.path import exists, join
from shutil import copyfile


class PullTester(Basic):
    def __init__(self, fixt):  # noqa: F811
        Basic.__init__(self, fixt)

    @property
    def pull(self):
        return self.menu.args(argv=["pull"])

    def __element(self, elem):
        return self.menu.args(argv=["pull", f"--e={elem}"])

    def massive(self):
        @assign_cli(self.pull, "pull")
        def wrapper():

            self.update_config_elements(*self.elements)

            output = PullCommand(self.root, self.home).main(self.pull)

            if output["code"] != "18":
                assert False

            for e in self.elements:
                if not exists(join(self.base.repo_path, e)):
                    assert False

            output = PullCommand(self.root, self.home).main(self.pull)

            if output["code"] != "17":
                assert False

        return wrapper()

    def specific_element(self, elem):
        @assign_cli(self.__element(elem), "pull")
        def wrapper():

            output = PullCommand(self.root, self.home).main(self.__element(elem))

            if output["code"] != "18":
                assert False

            output = PullCommand(self.root, self.home).main(self.__element(elem))

            if output["code"] != "16":
                assert False

            copyfile(join(self.home, "foo.txt"), join(self.home, self.elements[0]))

            output = PullCommand(self.root, self.home).main(self.__element(elem))

            if output["code"] != "37":
                assert False

        return wrapper()


def test_pull_massive(fixture):  # noqa: F811
    InitTester(fixture).run()
    pull = PullTester(fixture)
    pull.massive()


def test_pull_specific_element(fixture):  # noqa: F811
    InitTester(fixture).run()
    pull = PullTester(fixture)
    pull.specific_element(pull.elements[0])
