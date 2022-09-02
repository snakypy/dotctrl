from snakypy.helpers import FG, printer
from snakypy.helpers.console import billboard, credence

from snakypy.dotctrl import __info__
from snakypy.dotctrl.config.base import Base


class CreditsCommand(Base):
    def __init__(self, root, home):
        Base.__init__(self, root, home)

    def main(self):
        print("\n")
        printer(f'{self.msg["str:1"]}'.center(50), foreground=FG().GREEN)
        billboard(
            __info__["organization_name"], justify="center", foreground=FG().YELLOW
        )
        printer("Copyright (c) since 2020\n".center(100), foreground=FG().GREEN)
        credence(
            __info__["name"],
            __info__["version"],
            __info__["home_page"],
            __info__,
            foreground=FG().CYAN,
        )
