from .utilities import base  # noqa: E261,F401
from .test_link import link_massive
from snakypy.dotctrl.actions.unlink import UnlinkCommand
from snakypy.dotctrl.utils.decorators import assign_cli


def unlink_massive(base):  # noqa: F811
    args = base["Menu"].args(argv=["unlink"])
    # args_f = base["Menu"].args(argv=["unlink", "--f"])

    link_massive(base)

    @assign_cli(args, "unlink")
    def wrapper():

        out = UnlinkCommand(base["root"], base["home"]).main(args)

        if out["code"] != "31":
            assert False

        out = UnlinkCommand(base["root"], base["home"]).main(args)

        if out["code"] != "30":
            assert False

    return wrapper()


def unlink_element(base):  # noqa: F811
    args = base["Menu"].args(argv=["unlink", f"--e={base['elements'][0]}"])
    # args_f = base["Menu"].args(argv=["unlink", f"--e={base['elements'][0]}", "--f"])

    link_massive(base)

    @assign_cli(args, "unlink")
    def wrapper():

        out = UnlinkCommand(base["root"], base["home"]).main(args)

        if out["code"] != "12":
            assert False

        out = UnlinkCommand(base["root"], base["home"]).main(args)

        if out["code"] != "29":
            assert False

    return wrapper()


def test_unlink_massive(base):  # noqa: F811
    unlink_massive(base)


def test_unlink_element(base):  # noqa: F811
    unlink_element(base)
