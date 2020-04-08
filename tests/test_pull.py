from dotctrl.utils.decorators import assign_cli
from dotctrl.actions.pull import PullCommand
from os.path import exists, join, islink
from .utilities import (
    base,
    elements,
    update_config_elements,
    run_init_command,
    arguments,
    class_base,
)


@assign_cli(arguments(argv=["pull"]), "pull")
def test_pull_command(base):

    elements(base, create=True)

    run_init_command(base)

    update_config_elements(base, ".config/foo.txt", ".config/bar.txt")

    PullCommand(base["root"], base["home"]).main(
        arguments(argv=["pull", f"--element={elements(base)[0]}", "--force"])
    )

    file_linked = join(class_base(base).HOME, elements(base)[0])
    if islink(file_linked):
        assert False

    PullCommand(base["root"], base["home"]).main(arguments(argv=["pull"]))

    for item in elements(base):
        if not exists(join(class_base(base).repo_path, item)):
            assert False

    for item in class_base(base).editors_config:
        if not exists(join(class_base(base).repo_path, item)):
            assert False
