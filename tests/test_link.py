from os.path import islink, join

from snakypy.dotctrl.actions.link import LinkCommand
from snakypy.dotctrl.utils.decorators import assign_cli

from .test_pull import test_pull_command
from .utilities import base  # noqa: E261
from .utilities import arguments, class_base, elements


@assign_cli(arguments(argv=["link"]), "link")
def test_link_command(base):  # noqa: F811

    test_pull_command(base)

    LinkCommand(base["root"], base["home"]).main(
        arguments(argv=["link", f"--element={elements(base)[0]}", "--force"])
    )

    f = join(class_base(base).HOME, elements(base)[0])
    if not islink(f):
        assert False

    LinkCommand(base["root"], base["home"]).main(arguments(argv=["link", "--force"]))

    for item in elements(base):
        if not islink(join(class_base(base).HOME, item)):
            assert False

    for item in class_base(base).editors_config:
        if not islink(join(class_base(base).HOME, item)):
            assert False
