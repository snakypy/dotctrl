from dotctrl.utils.decorators import assign_cli
from os.path import exists
from .utilities import (
    base,
    elements,
    run_init_command,
    arguments,
    class_base,
)


@assign_cli(arguments(argv=["init"]), "init")
def test_init_command(base):

    elements(base, create=True)

    run_init_command(base)

    if not exists(class_base(base).config_path):
        assert False

    if not exists(class_base(base).repo_path):
        assert False
