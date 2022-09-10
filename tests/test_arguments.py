from snakypy.dotctrl.utils.decorators import assign_cli

from .utilities import Basic, fixture  # noqa: E261,F401


class ArgsTester:
    def __init__(self, fixt):  # noqa: F811
        Basic.__init__(self, fixt)

    def arguments(self, *args):
        return self.menu.args(argv=[*args])

    def run_init(self, *args):
        @assign_cli(self.arguments(*args), "init")
        def wrapper():
            return args

        return wrapper()

    def run_pull(self, *args):
        @assign_cli(self.arguments(*args), "pull")
        def wrapper():
            return args

        return wrapper()

    def main(self, *args):
        commands = {
            "init": self.run_init(*args),
            "pull": self.run_pull(*args),
        }

        return commands


def test_arguments(fixture):  # noqa: F811
    args = ArgsTester(fixture)

    init = args.main("init")
    init_git = args.main("init", "--git")
    init_auto = args.main("init", "--auto")

    if type(init["init"]) is not tuple:
        assert False

    if init["init"][0] != "init":
        assert False

    if type(init_git["init"]) is not tuple:
        assert False

    if type(init_auto["init"]) is not tuple:
        assert False

    if init_git["pull"] is not None:
        assert False

    if init_auto["pull"] is not None:
        assert False

    pull = args.main("pull")

    if type(pull["pull"]) is not tuple:
        assert False

    if pull["pull"][0] != "pull":
        assert False

    pull_element = args.main("pull", "--element=")

    if "--element=" not in pull_element["pull"]:
        assert False

    pull_e = args.main("pull", "--e=")

    if "--e=" not in pull_e["pull"]:
        assert False
