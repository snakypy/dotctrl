import pytest
import snakypy
from os.path import exists, islink, join, isfile
from dotctrl.utils.decorators import assign_cli
from dotctrl.config.base import Base
from dotctrl.actions.init import InitCommand
from dotctrl.actions.pull import PullCommand
from dotctrl.actions.link import LinkCommand
from dotctrl.actions.unlink import UnlinkCommand
from dotctrl.actions.restore import RestoreCommand
from dotctrl.utils import arguments


@pytest.fixture
def base(tmpdir):
    home = tmpdir.mkdir("home")
    root = tmpdir.mkdir("home/Dotfiles")
    for item in Base(root, home).editors_config:
        path_split = item.split("/")[:-1]
        path_str = "/".join(path_split)
        path = join(home, path_str)
        snakypy.path.create(path)
    return {"root": root, "home": home}


def class_base(base):
    inst = Base(base["root"], base["home"])
    return inst


def dotctrl_init(base):
    InitCommand(base["root"], base["home"]).main(arguments(argv=["init"]))


def dotfiles_tests(base, create=True):
    files_text = [".dotctrlrc", ".config/foo.txt"]
    if create:
        for item in files_text:
            snakypy.file.create("dotctrl tests", join(base["home"], item), force=True)
            if not exists(join(base["home"], item)):
                assert False
        for item in Base(base["root"], base["home"]).editors_config:
            snakypy.file.create("dotctrl tests", join(base["home"], item), force=True)
    return files_text


def update_config_elements(base, *files):
    parsed = class_base(base).parsed
    parsed["dotctrl"]["elements"] = [*files]
    parsed["dotctrl"]["smart"]["rc"]["enable"] = True
    parsed["dotctrl"]["smart"]["text_editors"]["enable"] = True
    snakypy.json.update(class_base(base).config_path, parsed)
    new_parsed = class_base(base).parsed
    assert new_parsed["dotctrl"]["elements"] == [*files]
    assert new_parsed["dotctrl"]["smart"]["rc"]["enable"] is True
    assert new_parsed["dotctrl"]["smart"]["text_editors"]["enable"] is True


def test_cli(base):
    dotfiles_tests(base)

    @assign_cli(arguments(argv=["init"]), "init")
    def init():
        dotctrl_init(base)
        if not exists(class_base(base).config_path):
            assert False
        if not exists(class_base(base).repo_path):
            assert False

    @assign_cli(arguments(argv=["pull"]), "pull")
    def pull():
        update_config_elements(base, ".config/foo.txt", ".config/bar.txt")
        PullCommand(base["root"], base["home"]).main(
            arguments(
                argv=[
                    "pull",
                    f"--element={dotfiles_tests(base, create=False)[0]}",
                    "--force",
                ]
            )
        )
        f = join(class_base(base).HOME, dotfiles_tests(base, create=False)[0])
        if islink(f):
            assert False
        PullCommand(base["root"], base["home"]).main(arguments(argv=["pull"]))
        for item in dotfiles_tests(base, create=False):
            if not exists(join(class_base(base).repo_path, item)):
                assert False
        for item in class_base(base).editors_config:
            if not exists(join(class_base(base).repo_path, item)):
                assert False

    @assign_cli(arguments(argv=["link"]), "link")
    def link():
        LinkCommand(base["root"], base["home"]).main(
            arguments(
                argv=[
                    "link",
                    f"--element={dotfiles_tests(base, create=False)[0]}",
                    "--force",
                ]
            )
        )
        f = join(class_base(base).HOME, dotfiles_tests(base, create=False)[0])
        if not islink(f):
            assert False
        LinkCommand(base["root"], base["home"]).main(
            arguments(argv=["link", "--force"])
        )
        for item in dotfiles_tests(base, create=False):
            if not islink(join(class_base(base).HOME, item)):
                assert False
        for item in class_base(base).editors_config:
            if not islink(join(class_base(base).HOME, item)):
                assert False

    @assign_cli(arguments(argv=["unlink"]), "unlink")
    def unlink():
        UnlinkCommand(base["root"], base["home"]).main(
            arguments(
                argv=["unlink", f"--element={dotfiles_tests(base, create=False)[0]}"]
            )
        )
        f = join(class_base(base).HOME, dotfiles_tests(base, create=False)[0])
        if islink(f):
            assert False

        with pytest.raises(SystemExit):
            UnlinkCommand(base["root"], base["home"]).main(arguments(argv=["unlink"]))

        UnlinkCommand(base["root"], base["home"]).main(
            arguments(argv=["unlink", "--force"])
        )
        for item in dotfiles_tests(base, create=False):
            if islink(join(class_base(base).HOME, item)):
                assert False
        for item in class_base(base).editors_config:
            if islink(join(class_base(base).HOME, item)):
                assert False

    @assign_cli(arguments(argv=["restore"]), "restore")
    def restore():
        RestoreCommand(base["root"], base["home"]).main(
            arguments(
                argv=[
                    "restore",
                    f"--element={dotfiles_tests(base, create=False)[0]}",
                    "--force",
                ]
            )
        )
        f = join(class_base(base).HOME, dotfiles_tests(base, create=False)[0])
        if not isfile(f):
            assert False

        with pytest.raises(SystemExit):
            RestoreCommand(base["root"], base["home"]).main(arguments(argv=["restore"]))

        RestoreCommand(base["root"], base["home"]).main(
            arguments(argv=["restore", "--force"])
        )
        for item in dotfiles_tests(base, create=False):
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

    init()
    pull()
    link()
    unlink()
    restore()
