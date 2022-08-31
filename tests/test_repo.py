from snakypy.dotctrl.actions.link import LinkCommand
from snakypy.dotctrl.actions.pull import PullCommand
from snakypy.dotctrl.actions.repo import RepoCommand
from snakypy.dotctrl.utils.decorators import assign_cli

from .utilities import base  # noqa: E261,F401
from .utilities import arguments, elements, run_init_command, update_config_elements


@assign_cli(arguments(argv=["repo", "--check"]), "repo")
def test_repo_check(base):  # noqa: F811
    elements(base, create=True)

    run_init_command(base)

    update_config_elements(base, rc=True, editors=True)

    PullCommand(base["root"], base["home"]).main(arguments(argv=["pull", "--f"]))

    if not RepoCommand(base["root"], base["home"]).main(
        arguments(argv=["repo", "--check"])
    ):
        assert True

    LinkCommand(base["root"], base["home"]).main(arguments(argv=["link", "--force"]))

    if not RepoCommand(base["root"], base["home"]).main(
        arguments(argv=["repo", "--check"])
    ):
        assert False


@assign_cli(arguments(argv=["repo", "--imported"]), "repo")
def test_repo_imported(base):  # noqa: F811
    elements(base, create=True)

    run_init_command(base)

    if RepoCommand(base["root"], base["home"]).main(
        arguments(argv=["repo", "--imported"])
    ):
        assert False

    update_config_elements(
        base, ".config/foo.txt", ".config/bar.txt", rc=True, editors=True
    )

    PullCommand(base["root"], base["home"]).main(arguments(argv=["pull", "--f"]))

    LinkCommand(base["root"], base["home"]).main(arguments(argv=["link", "--f"]))

    if not RepoCommand(base["root"], base["home"]).main(
        arguments(argv=["repo", "--imported"])
    ):
        assert False
