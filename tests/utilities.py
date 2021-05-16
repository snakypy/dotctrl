import pytest
from snakypy.helpers.path import create as create_path
from snakypy.helpers.files import create_file, update_json
from os.path import exists, join
from snakypy.dotctrl.config.base import Base
from snakypy.dotctrl.actions.init import InitCommand
from snakypy.dotctrl.utils import arguments


@pytest.fixture
def base(tmpdir):
    home = tmpdir.mkdir("home")
    root = tmpdir.mkdir("home/Dotfiles")
    for item in Base(root, home).editors_config:
        path_split = item.split("/")[:-1]
        path_str = "/".join(path_split)
        path = join(home, path_str)
        create_path(path)
    return {"root": root, "home": home}


def class_base(base):
    inst = Base(base["root"], base["home"])
    return inst


def run_init_command(base):
    InitCommand(base["root"], base["home"]).main(arguments(argv=["init"]))


def elements(base, create=False):
    elements_lst = [".dotctrlrc", ".config/foo.txt"]
    if create:
        for elem in elements_lst:
            create_file("dotctrl tests", join(base["home"], elem), force=True)
            if not exists(join(base["home"], elem)):
                assert False
        for file in Base(base["root"], base["home"]).editors_config:
            create_file("dotctrl tests", join(base["home"], file), force=True)
    return elements_lst


def update_config_elements(base, *files):
    parsed = class_base(base).parsed
    parsed["dotctrl"]["elements"] = [*files]
    parsed["dotctrl"]["smart"]["rc"]["enable"] = True
    parsed["dotctrl"]["smart"]["text_editors"]["enable"] = True
    update_json(class_base(base).config_path, parsed)
    new_parsed = class_base(base).parsed
    assert new_parsed["dotctrl"]["elements"] == [*files]
    assert new_parsed["dotctrl"]["smart"]["rc"]["enable"] is True
    assert new_parsed["dotctrl"]["smart"]["text_editors"]["enable"] is True
