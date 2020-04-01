import pytest
import snakypy
from os.path import exists, join, islink
from dotctrl.dotctrl import Dotctrl
from dotctrl import decorators


@pytest.fixture
def base(tmpdir):
    home = tmpdir.mkdir("home")
    root = tmpdir.mkdir("home/Dotfiles")
    inst = Dotctrl(root, home)
    for item in inst.text_editors:
        path_split = item.split("/")[:-1]
        path_str = "/".join(path_split)
        path = join(home, path_str)
        snakypy.path.create(path)
    return {"root": root, "home": home}


def class_dotctrl(base):
    inst = Dotctrl(base["root"], base["home"])
    return inst


def dotctrl_init(base):
    return class_dotctrl(base).init_command()


def dotfiles_tests(base, create=True):
    files_text = [".dotctrlrc", ".config/foo.txt"]
    if create:
        for item in files_text:
            snakypy.file.create("dotctrl tests", join(base["home"], item), force=True)
            if not exists(join(base["home"], item)):
                assert False
        for item in class_dotctrl(base).text_editors:
            snakypy.file.create("dotctrl tests", join(base["home"], item))
    return files_text


def update_config_elements(base, *files):
    parsed = class_dotctrl(base).parsed
    parsed["dotctrl"]["elements"] = [*files]
    parsed["dotctrl"]["smart"]["rc"]["enable"] = True
    parsed["dotctrl"]["smart"]["text_editors"]["enable"] = True
    snakypy.json.update(class_dotctrl(base).config, parsed)
    new_parsed = class_dotctrl(base).parsed
    assert new_parsed["dotctrl"]["elements"] == [*files]
    assert new_parsed["dotctrl"]["smart"]["rc"]["enable"] is True
    assert new_parsed["dotctrl"]["smart"]["text_editors"]["enable"] is True


def test_cli(base):
    dotfiles_tests(base)

    @decorators.assign_cli(class_dotctrl(base).arguments(argv=["init"]), "init")
    def init():
        dotctrl_init(base)
        if not exists(class_dotctrl(base).config):
            assert False
        if not exists(class_dotctrl(base).repo):
            assert False

    @decorators.assign_cli(
        class_dotctrl(base).arguments(argv=["--credits"]), "--credits"
    )
    def credence():
        class_dotctrl(base).credence()

    @decorators.assign_cli(class_dotctrl(base).arguments(argv=["pull"]), "pull")
    def pull():
        update_config_elements(base, ".config/foo.txt", ".config/bar.txt")
        class_dotctrl(base).pull_command(force=True)
        for item in dotfiles_tests(base, create=False):
            if not exists(join(class_dotctrl(base).repo, item)):
                assert False
        for item in class_dotctrl(base).text_editors:
            if not exists(join(class_dotctrl(base).repo, item)):
                assert False

    @decorators.assign_cli(class_dotctrl(base).arguments(argv=["check"]), "check")
    def check():
        class_dotctrl(base).check_command()

    @decorators.assign_cli(class_dotctrl(base).arguments(argv=["link"]), "link")
    def link():
        class_dotctrl(base).link_command(force=True)
        for item in dotfiles_tests(base, create=False):
            if not islink(join(class_dotctrl(base).HOME, item)):
                assert False
        for item in class_dotctrl(base).text_editors:
            if not islink(join(class_dotctrl(base).HOME, item)):
                assert False

    @decorators.assign_cli(class_dotctrl(base).arguments(argv=["unlink"]), "unlink")
    def unlink():
        class_dotctrl(base).unlink_command()
        for item in dotfiles_tests(base, create=False):
            if islink(join(class_dotctrl(base).HOME, item)):
                assert False
        for item in class_dotctrl(base).text_editors:
            if islink(join(class_dotctrl(base).HOME, item)):
                assert False

    @decorators.assign_cli(class_dotctrl(base).arguments(argv=["restore"]), "restore")
    def restore():
        class_dotctrl(base).restore_command()
        for item in dotfiles_tests(base, create=False):
            if exists(join(class_dotctrl(base).repo, item)):
                assert False
        for item in class_dotctrl(base).text_editors:
            if exists(join(class_dotctrl(base).repo, item)):
                assert False
        for item in class_dotctrl(base).text_editors:
            if islink(join(class_dotctrl(base).HOME, item)):
                assert False

    init()
    credence()
    pull()
    link()
    unlink()
    check()
    restore()
