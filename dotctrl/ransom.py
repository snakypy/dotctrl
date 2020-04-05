"""Modulate to store records and data."""
import sys
import snakypy
from os.path import exists, join
from snakypy import FG, printer
from dotctrl import __pkginfo__, utils


class Ransom:
    """Class to retrieve data"""

    def __init__(self, root, home):
        self.ROOT = root
        self.HOME = home
        self.repo = join(self.ROOT, "dotctrl")
        self.config = join(self.ROOT, __pkginfo__["config"])
        self.gitignore = join(self.ROOT, ".gitignore")
        self.readme = join(self.ROOT, "README.md")
        self.text_editors = [
            ".config/Code/User/settings.json",
            ".config/Code/User/locale.json",
            ".atom/config.cson",
            ".atom/github.cson",
            ".atom/snippets.cson",
            ".config/sublime-text-3/Packages/User/" "Preferences.sublime-settings",
            ".config/sublime-text-3/Packages/User/" "Package Control.sublime-settings",
            ".config/sublime-text-3/Packages/User/" "Distraction Free.sublime-settings",
        ]

        if exists(self.config):
            try:
                self.parsed = snakypy.json.read(self.config)
                self.elements = [*self.parsed["dotctrl"]["elements"]]
                self.rc_status = self.parsed["dotctrl"]["smart"]["rc"]["enable"]
                self.text_editors_status = self.parsed["dotctrl"]["smart"][
                    "text_editors"
                ]["enable"]
            except FileNotFoundError as f:
                printer(f"Configuration file not found.", f, foreground=FG.ERROR)
            except Exception as e:
                printer(
                    "An error occurred while reading the configuration file.",
                    e,
                    foreground=FG.ERROR,
                )
                sys.exit(1)

            rc = utils.listing_files(self.HOME, only_rc=True)

            if self.rc_status and self.text_editors_status:
                self.data = rc + self.text_editors + self.elements
            elif self.rc_status and not self.text_editors_status:
                self.data = rc + self.elements
            elif not self.rc_status and self.text_editors_status:
                self.data = self.text_editors + self.elements
            else:
                self.data = self.elements
