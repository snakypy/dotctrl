import pytest
from dotctrl.utils.decorators import assign_cli
from dotctrl.actions.unlink import UnlinkCommand
from os.path import join, islink
from .utilities import (
    base,
    elements,
    arguments,
    class_base,
)
from .test_link import test_link_command


@assign_cli(arguments(argv=["unlink"]), "unlink")
def test_unlink_command(base):

    test_link_command(base)

    UnlinkCommand(base["root"], base["home"]).main(
        arguments(argv=["unlink", f"--element={elements(base)[0]}"])
    )

    linked_file = join(class_base(base).HOME, elements(base)[0])
    if islink(linked_file):
        assert False

    with pytest.raises(SystemExit):
        UnlinkCommand(base["root"], base["home"]).main(arguments(argv=["unlink"]))

    UnlinkCommand(base["root"], base["home"]).main(
        arguments(argv=["unlink", "--force"])
    )

    for item in elements(base):
        if islink(join(class_base(base).HOME, item)):
            assert False

    for item in class_base(base).editors_config:
        if islink(join(class_base(base).HOME, item)):
            assert False
