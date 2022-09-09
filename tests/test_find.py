from .utilities import base  # noqa: E261,F401
from .test_pull import pull_massive
from snakypy.dotctrl.utils.decorators import assign_cli
from snakypy.dotctrl.actions.find import FindCommand


# TODO: Find bug test
def find_element(base):  # noqa: F811
    args = base["Menu"].args(argv=["find", f"--name={base['elements'][0]}"])
    args_not = base["Menu"].args(argv=["find", "--name=notexists.txt"])

    @assign_cli(args, "find")
    def wrapper():
        pull_massive(base)

        out = FindCommand(base["root"], base["home"]).main(args)

        # if out["code"] != "03":
        #     assert False

        print(">>>>>>>>>>>", out)

        # out = FindCommand(base["root"], base["home"]).main(args_not)

        # if out["code"] != "04":
        #     assert False

    return wrapper()


def test_find_element(base):  # noqa: F811
    find_element(base)
