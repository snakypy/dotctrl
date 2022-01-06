from snakypy.dotctrl.actions.find import FindCommand
from snakypy.dotctrl.actions.link import LinkCommand
from snakypy.dotctrl.actions.pull import PullCommand
from snakypy.dotctrl.utils.decorators import assign_cli

from .utilities import base  # noqa: E261
from .utilities import arguments, elements, run_init_command, update_config_elements


@assign_cli(arguments(argv=["find", '--name=""']), "find")
def test_find(base):  # noqa: F811
    elements(base, create=True)

    run_init_command(base)

    update_config_elements(base, rc=True, editors=True)

    PullCommand(base["root"], base["home"]).main(arguments(argv=["pull", "--force"]))

    LinkCommand(base["root"], base["home"]).main(arguments(argv=["link", "--force"]))

    if not FindCommand(base["root"], base["home"]).main(
        arguments(argv=["find", f'--name="{elements(base)[0]}"'])
    ):
        assert False
