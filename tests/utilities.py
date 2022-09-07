from os.path import join

import pytest
from snakypy.helpers.files import create_file, update_json, read_json

from snakypy.dotctrl.config.base import Base
from snakypy.dotctrl.utils import path_creation

# from snakypy.dotctrl.utils import arguments
from snakypy.dotctrl.config.menu import Menu


@pytest.fixture
def base(tmpdir):
    home = tmpdir.mkdir("home")
    root = tmpdir.mkdir(join("home", "dotfiles"))
    base = Base(root, home)
    menu = Menu(root, home)

    elements = ["bar.txt", ".config/foo.txt"]

    for e in elements:
        if "/" in e:
            path_creation(home, e)
        create_file("dotctrl tests", join(home, e), force=True)

    create_file("Intruder", join(home, "intruder.txt"), force=True)

    return {
        "root": root,
        "home": home,
        "Base": base,
        "Menu": menu,
        "elements": elements,
    }


def add_elements(base, *args):
    parsed = read_json(base["Base"].config_path)
    parsed["dotctrl"]["elements"] = [*args]
    update_json(base["Base"].config_path, parsed)


# def elements(base, create: bool = False):
#     lst = [".myrc", ".config/foo.txt"]
#     if create:
#         for e in lst:
#             if "/" in e:
#                 path_creation(base["home"], e)
#             create_file("dotctrl tests", join(base["home"], e), force=True)
#             if not exists(join(base["home"], e)):
#                 assert False
#     return lst


# def class_base(base):
#     return Base(base["root"], base["home"])


# def run_init_command(base):
#     args = base["menu"].arguments(argv=["init"])
#     InitCommand(base["root"], base["home"]).main(args)


# def update_config_elements(base, *files, rc=True, editors=True):
#     parsed = class_base(base).parsed
#     parsed["dotctrl"]["elements"] = [*files]
#     update_json(class_base(base).config_path, parsed)
#     new_parsed = class_base(base).parsed
#     assert new_parsed["dotctrl"]["elements"] == [*files]
