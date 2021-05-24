from snakypy.dotctrl.actions.link import LinkCommand
from snakypy.dotctrl.actions.list import ListCommand
from snakypy.dotctrl.actions.pull import PullCommand
from .utilities import arguments, elements, run_init_command, update_config_elements
from snakypy.dotctrl.utils.decorators import assign_cli
from .utilities import base  # noqa: E261


@assign_cli(arguments(argv=["list"]), "list")
def test_list(base):
    elements(base, create=True)

    run_init_command(base)

    if ListCommand(base["root"], base["home"]).main():
        assert False

    update_config_elements(base, ".config/foo.txt", ".config/bar.txt", rc=True, editors=True)

    PullCommand(base["root"], base["home"]).main(
        arguments(argv=["pull", "--force"])
    )

    LinkCommand(base["root"], base["home"]).main(
        arguments(argv=["link", "--force"])
    )

    if not ListCommand(base["root"], base["home"]).main():
        assert False
