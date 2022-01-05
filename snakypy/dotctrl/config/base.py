"""Modulate to store records and data."""
import sys
from os.path import exists, join
from sys import exit, platform

from snakypy.helpers import FG, printer
from snakypy.helpers.files import read_json

from snakypy.dotctrl import __info__, utils


class Base:
    """Class to retrieve data"""

    def __init__(self, root, home):
        self.ROOT = root
        self.HOME = home
        self.repo_path = join(self.ROOT, "dotctrl")
        self.config_path = join(self.ROOT, __info__["config"])
        self.gitignore_path = join(self.ROOT, ".gitignore_path")
        self.readme = join(self.ROOT, "README.md")
        self.atom = [".atom/config.cson", ".atom/github.cson", ".atom/snippets.cson"]
        self.vscode_data = {
            "linux": [
                ".config/Code/User/settings.json",
                ".config/Code/User/locale.json",
            ],
            "macos": [
                "Library/Application Support/Code/User/settings.json",
                "Library/Application Support/Code/User/locale.json",
            ],
        }
        self.vscode = (
            self.vscode_data["linux"]
            if platform == "linux"
            else self.vscode_data["macos"]
        )

        self.sublime_data = {
            "linux": [
                ".config/sublime-text/Packages/User/" "Preferences.sublime-settings",
                ".config/sublime-text/Packages/User/"
                "Package Control.sublime-settings",
                ".config/sublime-text/Packages/User/"
                "Distraction Free.sublime-settings",
            ],
            "macos": [
                "Library/Application Support/Sublime Text/Packages/User/"
                "Preferences.sublime-settings",
                "Library/Application Support/Sublime Text/Packages/User/"
                "Package Control.sublime-settings",
                "Library/Application Support/Sublime Text/Packages/User/"
                "Distraction Free.sublime-settings",
            ],
        }

        self.sublime = (
            self.sublime_data["linux"]
            if platform == "linux"
            else self.sublime_data["macos"]
        )

        self.editors_config = self.atom + self.vscode + self.sublime

        if exists(self.config_path):
            try:
                self.parsed = read_json(self.config_path)
                self.elements = list(self.parsed["dotctrl"]["elements"])
                self.rc_files = utils.listing_files(self.HOME, only_rc_files=True)
                self.rc_files_status = self.parsed["dotctrl"]["smart"]["rc"]["enable"]
                self.text_editors_status = self.parsed["dotctrl"]["smart"][
                    "text_editors"
                ]["enable"]
            except FileNotFoundError as err:
                printer(
                    "Configuration file not found.", str(err), foreground=FG().ERROR
                )
            except Exception as err:
                printer(
                    "An error occurred while reading the configuration file.",
                    str(err),
                    foreground=FG().ERROR,
                )
                exit(1)

            if self.rc_files_status and self.text_editors_status:
                self.data: list = self.rc_files + self.editors_config + self.elements
            elif self.rc_files_status and not self.text_editors_status:
                self.data = self.rc_files + self.elements
            elif not self.rc_files_status and self.text_editors_status:
                self.data = self.editors_config + self.elements
            else:
                self.data = self.elements
