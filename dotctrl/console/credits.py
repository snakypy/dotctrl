import snakypy
from dotctrl import __version__
from dotctrl.config import package
from snakypy import printer, FG


class Command:
    @staticmethod
    def main():
        print("\n")
        printer("Offered by:".center(50), foreground=FG.GREEN)
        snakypy.console.billboard(
            package.info["organization_name"], justify="center", foreground=FG.YELLOW
        )
        printer(f"copyright (c) since 2020\n".center(100), foreground=FG.GREEN)
        snakypy.console.credence(
            package.info["name"],
            __version__,
            package.info["home_page"],
            package.info,
            foreground=FG.CYAN,
        )
