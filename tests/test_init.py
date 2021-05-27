from os.path import exists

from snakypy.dotctrl.utils.decorators import assign_cli

from .utilities import base  # noqa: E261
from .utilities import arguments, class_base, elements, run_init_command


@assign_cli(arguments(argv=["init"]), "init")
def test_init_command(base):  # noqa: F811

    elements(base, create=True)

    run_init_command(base)

    if not exists(class_base(base).config_path):
        assert False

    if not exists(class_base(base).repo_path):
        assert False
