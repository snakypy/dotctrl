from os.path import islink, join

import pytest

from snakypy.dotctrl.actions.unlink import UnlinkCommand
from snakypy.dotctrl.utils.decorators import assign_cli

from .test_link import test_link_command
from .utilities import base  # noqa: E261,F401
from .utilities import arguments, class_base, elements


@assign_cli(arguments(argv=["unlink"]), "unlink")
def test_unlink_command(base):  # noqa: F811

    test_link_command(base)

    UnlinkCommand(base["root"], base["home"]).main(
        arguments(argv=["unlink", f"--e={elements(base)[0]}"])
    )

    linked_file = join(class_base(base).HOME, elements(base)[0])
    if islink(linked_file):
        assert False

    with pytest.raises(SystemExit):
        UnlinkCommand(base["root"], base["home"]).main(arguments(argv=["unlink"]))

    UnlinkCommand(base["root"], base["home"]).main(arguments(argv=["unlink", "--f"]))

    for item in elements(base):
        if islink(join(class_base(base).HOME, item)):
            assert False

    for item in class_base(base).editors_config:
        if islink(join(class_base(base).HOME, item)):
            assert False
