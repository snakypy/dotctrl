from os.path import join

import pytest
from snakypy.helpers.files import create_file, read_json, update_json
from snakypy.helpers.path import create as create_path

from snakypy.dotctrl.config.base import Base
from snakypy.dotctrl.config.menu import Menu
from snakypy.dotctrl.utils import path_creation


def populate_home(path: str) -> list:
    files: list = ["bar.txt", ".config/foo.txt"]

    folders: list = [".config/bar"]

    for f in files:
        if "/" in f:
            path_creation(path, f)
        create_file("Example", join(path, f), force=True)

    create_file("Foo", join(path, "foo.txt"), force=True)

    for folder in folders:
        create_path(join(path, folder))

    return files + folders


@pytest.fixture
def fixture(tmpdir):
    home = tmpdir.mkdir("home")
    root = tmpdir.mkdir(join("home", "dotfiles"))
    base = Base(root, home)
    menu = Menu(root, home)

    return {
        "root": root,
        "home": home,
        "base": base,
        "menu": menu,
        "elements": populate_home(home),
    }


class Basic:
    def __init__(self, fixt):  # noqa: F811
        self.home = fixt["home"]
        self.root = fixt["root"]
        self.base = fixt["base"]
        self.menu = fixt["menu"]
        self.elements = fixt["elements"]

    def update_config_elements(self, *args):
        parsed = read_json(self.base.config_path)
        parsed["dotctrl"]["elements"] = [*args]
        update_json(self.base.config_path, parsed)
