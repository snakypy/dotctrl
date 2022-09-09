from os.path import exists

from snakypy.dotctrl.utils.decorators import assign_cli
from snakypy.dotctrl.actions.init import InitCommand

from .utilities import base  # noqa: E261, F401


def test_init(base):  # noqa: F811
    args = base["Menu"].args(argv=["init"])

    @assign_cli(args, "init")
    def wrapper():
        InitCommand(base["root"], base["home"]).main(args)

        if not exists(base["Base"].config_path):
            assert False

        if not exists(base["Base"].repo_path):
            assert False

    return wrapper()


# WHITOUT DECORATOR
# def test_init_command(base):  # noqa: F811

#     args = base["Menu"].args(argv=["init"])
#     InitCommand(base["root"], base["home"]).main(args)

#     if not exists(base["Base"].config_path):
#         assert False

#     if not exists(base["Base"].repo_path):
#         assert False
