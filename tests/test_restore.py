from os.path import exists, isfile, islink, join

from snakypy.helpers.files.json import read_json

from snakypy.dotctrl.actions.restore import RestoreCommand
from snakypy.dotctrl.utils.decorators import assign_cli

from .test_unlink import test_unlink_command
from .utilities import base  # noqa: E261, F401
from .utilities import arguments, class_base, elements


@assign_cli(arguments(argv=["restore"]), "restore")
def test_restore_command(base):  # noqa: F811

    test_unlink_command(base)

    RestoreCommand(base["root"], base["home"]).main(
        arguments(argv=["restore", f"--e={elements(base)[1]}", "--f"])
    )

    linked_file = join(class_base(base).HOME, elements(base)[1])
    if not isfile(linked_file):
        assert False

    RestoreCommand(base["root"], base["home"]).main(arguments(argv=["restore", "--f"]))

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

    # test: keep_record
    RestoreCommand(base["root"], base["home"]).main(
        arguments(
            argv=[
                "restore",
                f"--element={elements(base)[1]}",
                "--force",
                "--keep-record",
            ]
        )
    )

    parsed = read_json(class_base(base).config_path)
    if elements(base)[1] in parsed["dotctrl"]["elements"]:
        assert False
