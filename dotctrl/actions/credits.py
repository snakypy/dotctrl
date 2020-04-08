from snakypy.console import credence, billboard
from dotctrl import __version__
from dotctrl.config import package
from snakypy import printer, FG


class CreditsCommand:
    @staticmethod
    def main():
        print("\n")
        printer("Offered by:".center(50), foreground=FG.GREEN)
        billboard(
            package.info["organization_name"], justify="center", foreground=FG.YELLOW
        )
        printer(f"copyright (c) since 2020\n".center(100), foreground=FG.GREEN)
        credence(
            package.info["name"],
            __version__,
            package.info["home_page"],
            package.info,
            foreground=FG.CYAN,
        )
