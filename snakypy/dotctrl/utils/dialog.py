from snakypy.helpers import FG, NONE, printer


def pick_options(
    title: str,
    options: list,
    answer: str,
    *,
    colorful: bool = False,
    index: bool = False,
    lowercase: bool = False,
    ctrl_c_message: bool = False,
    cancel_msg: str,
    invalid_msg: str,
):
    if not colorful:
        FG().QUESTION = ""
        FG().GREEN = ""
        FG().MAGENTA = ""
        FG().CYAN = ""
        FG().ERROR = ""
        FG().WARNING = ""

    ctrl_c = "(Ctrl+C to Cancel)" if ctrl_c_message else ""

    printer(title, ctrl_c, foreground=FG(question_icon="\n-> ").QUESTION)

    count = 1

    for option in options:
        print(f"{FG().GREEN}[{count}] {FG().MAGENTA}{option}{NONE}")
        count += 1

    try:
        pos = int(input(f"{FG().CYAN}{answer} {NONE}")) - 1
        assert pos > -1
        if index and lowercase:
            return pos, options[pos].lower()
        elif index and not lowercase:
            return pos, options[pos]
        if lowercase:
            return options[pos].lower()
        return options[pos]

    except (IndexError, ValueError):
        printer(invalid_msg, foreground=FG(error_icon="[x] ").ERROR)
        return False

    except KeyboardInterrupt:
        printer(cancel_msg, foreground=FG(warning_icon=" [!] ").WARNING)
        return None


def pick(
    title: str,
    options: list,
    *,
    answer: str = "Answer:",
    index: bool = False,
    colorful: bool = False,
    lowercase: bool = False,
    ctrl_c_message: bool = False,
    cancel_msg: str = "Canceled by user.",
    invalid_msg: str = "Option invalid!",
):

    if not type(options) is list:
        raise TypeError("You must enter a list in the argument: options")

    if len(title) == 0:
        raise TypeError("The title cannot contain an empty element. Approached.")

    for option in options:
        if len(option) == 0:
            raise TypeError("The list cannot contain an empty element. Approached.")

    try:

        while True:
            option = pick_options(
                title,
                options,
                answer=answer,
                index=index,
                colorful=colorful,
                lowercase=lowercase,
                ctrl_c_message=ctrl_c_message,
                cancel_msg=cancel_msg,
                invalid_msg=invalid_msg,
            )
            if option or option is None:
                break
        return option

    except Exception:
        raise Exception("An unexpected error occurs when using pick")
