"""Module menu"""
from snakypy.helpers import FG
from snakypy.helpers.ansi import NONE

from snakypy.dotctrl import __info__

# Messages colorful
DANGER = f"{FG().YELLOW}DANGER!{NONE}"

# Menu options and arguments.
options = f"""
{__info__['name']} version: {FG().CYAN}{__info__['version']}{NONE}

{__info__['name']} - Managing your dotfiles on Linux.

USAGE:
    {__info__['executable']} init [--auto | --git]
    {__info__['executable']} repo (--check | --imported | --info)
    {__info__['executable']} find (--name=<object>)
    {__info__['executable']} pull [--element=<object>] [--force]
    {__info__['executable']} link [--element=<object>] [--force]
    {__info__['executable']} unlink [--element=<object>] [--force]
    {__info__['executable']} config (--open | --view)
    {__info__['executable']} restore [--element=<object>] [--force] [--rm-registry]
    {__info__['executable']} --help
    {__info__['executable']} --version
    {__info__['executable']} --credits

ARGUMENTS:
    {FG().CYAN}init{NONE} ----------- Creates the dotfiles repository.
    {FG().CYAN}find{NONE} ----------- Find some object in the Dotctrl repository.
    {FG().CYAN}pull{NONE} ----------- Pulls the dotfiles from the source location on the
                     machine to the repository.
    {FG().CYAN}link{NONE} ----------- Links the repository's dotfiles to the source location
                     on the machine.
    {FG().CYAN}repo{NONE} ----------- Show {__info__["name"]} repository information.
    {FG().CYAN}unlink{NONE} --------- Unlink the dotfiles from the repository with the original location
                     on the machine.
    {FG().CYAN}config{NONE} --------- Handles the configuration file.
    {FG().CYAN}restore{NONE} -------- Moves all dotfiles from the repository to the default source location.

OPTIONS:
    {FG().BLUE}--check{NONE} --------------- Checks whether the dotfiles in the repository are linked to
                            the place of origin or not.
    {FG().BLUE}--element=<object>{NONE} ---- Receives an object without its absolute path, just the relative one.
    {FG().BLUE}--open{NONE} ---------------- Open a file in edit mode.
    {FG().BLUE}--view{NONE} ---------------- View the contents of a file in the terminal.
    {FG().BLUE}--git{NONE} ----------------- Create a Git repository.
    {FG().BLUE}--auto{NONE} ---------------- Creates the {__info__["name"]} repository automatically in the users
                            directory. On Linux it will create in "/home", on macOS in "/Users".
                            You must have super user permission.
    {FG().BLUE}--info{NONE} ---------------- Shows detailed information for the Do Ctrl repository.
    {FG().BLUE}--imported{NONE} ------------ Lists imported elements.
    {FG().BLUE}--name=<object>{NONE} ------- Receives the name of an object, it can be a folder or a file.
    {FG().BLUE}--force{NONE} --------------- Complete the command regardless of whether or not files exist.
                             ATTENTION! Using this option will replace existing files.
    {FG().BLUE}--rm-registry{NONE} ---------- Removes the object in the {__info__["name"]} registry
                                             ({__info__["config"]}).
    {FG().BLUE}--version{NONE} ------------- Show version.
    {FG().BLUE}--credits{NONE} ------------- Show credits.
    {FG().BLUE}--help{NONE} ---------------- Show this screen.
"""
