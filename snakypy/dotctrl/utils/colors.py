from snakypy.helpers import FG, NONE, SGR


class Colors:
    GREEN: str = FG().GREEN
    YELLOW: str = FG().YELLOW
    RED: str = FG().RED
    MAGENTA: str = FG().MAGENTA
    BLUE: str = FG().BLUE
    CYAN: str = FG().CYAN
    BOLD: str = SGR().BOLD
    UNDERLINE: str = SGR().UNDERLINE
    WARNING: str = FG(warning_icon="[!] ").WARNING
    FINISH: str = FG().FINISH
    ERROR: str = FG(error_icon="[x] ").ERROR
    QUESTION: str = FG(question_icon="-> ").QUESTION

    @staticmethod
    def none(element: str, reset: str = NONE, end: str = "") -> str:
        return f"{NONE}{element}{reset}{end}"

    def cyan(self, element: str, reset: str = NONE, end: str = "") -> str:
        return f"{self.CYAN}{element}{reset}{end}"

    def green(self, element: str, reset: str = NONE, end: str = "") -> str:
        return f"{self.GREEN}{element}{reset}{end}"

    def blue(self, element: str, reset: str = NONE, end: str = "") -> str:
        return f"{self.BLUE}{element}{reset}{end}"

    def red(self, element: str, reset: str = NONE, end: str = "") -> str:
        return f"{self.RED}{element}{reset}{end}"

    def yellow(self, element: str, reset: str = NONE, end: str = "") -> str:
        return f"{self.YELLOW}{element}{reset}{end}"

    def magenta(self, element: str, reset: str = NONE, end: str = "") -> str:
        return f"{self.MAGENTA}{element}{reset}{end}"

    def bold(self, element: str, reset: str = NONE, end: str = "") -> str:
        return f"{self.BOLD}{element}{reset}{end}"

    def underline(self, element: str, reset: str = NONE, end: str = "") -> str:
        return f"{self.UNDERLINE}{element}{reset}{end}"
