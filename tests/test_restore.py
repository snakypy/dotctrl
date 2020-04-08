import pytest
from dotctrl.utils.decorators import assign_cli
from dotctrl.actions.restore import RestoreCommand
from os.path import join, islink, exists, isfile
from .utilities import (
    base,
    elements,
    arguments,
    class_base,
)
from .test_unlink import test_unlink_command


@assign_cli(arguments(argv=["restore"]), "restore")
def test_restore_command(base):

    test_unlink_command(base)

    RestoreCommand(base["root"], base["home"]).main(
        arguments(argv=["restore", f"--element={elements(base)[0]}", "--force"])
    )

    linked_file = join(class_base(base).HOME, elements(base)[0])
    if not isfile(linked_file):
        assert False

    with pytest.raises(SystemExit):
        RestoreCommand(base["root"], base["home"]).main(arguments(argv=["restore"]))

    RestoreCommand(base["root"], base["home"]).main(
        arguments(argv=["restore", "--force"])
    )

    for item in elements(base):
        elem_repo = join(class_base(base).repo_path, item)
        if exists(elem_repo):
            assert False

    for item in class_base(base).editors_config:
        elem_repo = join(class_base(base).repo_path, item)
        if exists(elem_repo):
            assert False
    for item in class_base(base).editors_config:
        elem_home = join(class_base(base).HOME, item)
        if islink(elem_home):
            assert False
