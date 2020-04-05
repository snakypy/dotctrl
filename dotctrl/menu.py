""""""
from snakypy import FG
from snakypy.ansi import NONE
from dotctrl import __pkginfo__, __version__

# Messages colorful
DANGER = f"{FG.YELLOW}DANGER!{NONE}"

# Menu options and arguments.
menu_opts = f"""
{__pkginfo__['name']} version: {FG.CYAN}{__version__}{NONE}

{__pkginfo__['name']} - Managing your dotfiles on Linux.

USAGE:
    {__pkginfo__['executable']} init [--git]
    {__pkginfo__['executable']} check
    {__pkginfo__['executable']} list
    {__pkginfo__['executable']} pull [--element=<object>] [--force]
    {__pkginfo__['executable']} link [--element=<object>] [--force]
    {__pkginfo__['executable']} unlink [--element=<object>]
    {__pkginfo__['executable']} config (--open | --view)
    {__pkginfo__['executable']} restore [--element=<object>] [--force]
    {__pkginfo__['executable']} remove [--all] [--noconfirm]
    {__pkginfo__['executable']} --help
    {__pkginfo__['executable']} --version
    {__pkginfo__['executable']} --credits

ARGUMENTS:
    {FG.CYAN}init{NONE} ----------- Creates the dotfiles repository.
    {FG.CYAN}pull{NONE} ----------- Pulls the dotfiles from the source location on the
                     machine to the repository.
    {FG.CYAN}link{NONE} ----------- Links the repository's dotfiles to the source location
                     on the machine.
    {FG.CYAN}check{NONE} ---------- Checks whether the dotfiles in the repository are linked to
                     the place of origin or not.
    {FG.CYAN}list{NONE} ----------- Lists all files present in the repository and in the configuration.
    {FG.CYAN}unlink{NONE} --------- Unlink the dotfiles from the repository with the original location
                     on the machine.
    {FG.CYAN}config{NONE} --------- Handles the configuration file.
    {FG.CYAN}restore{NONE} -------- Moves all dotfiles from the repository to the default source location.
    {FG.CYAN}remove{NONE} --------- {DANGER} Removes the elements in the repository and symbolic link in
                     the source location.

OPTIONS:
    {FG.BLUE}--element=<object>{NONE} ---- Receive an object where, have the absolute path to a file or
                            folder, always from the HOME directory.
    {FG.BLUE}--open{NONE} ---------------- Open a file in edit mode.
    {FG.BLUE}--view{NONE} ---------------- View the contents of a file in the terminal.
    {FG.BLUE}--git{NONE} ----------------- Create a Git repository.
    {FG.BLUE}--force{NONE} --------------- Complete the command regardless of whether or not files exist.
    {FG.BLUE}--all{NONE} ----------------- Perform a mass action.
    {FG.BLUE}--noconfirm{NONE} ----------- {DANGER} Perform an action without calling a confirmation.
    {FG.BLUE}--version{NONE} ------------- Show version.
    {FG.BLUE}--credits{NONE} ------------- Show credits.
    {FG.BLUE}--help{NONE} ---------------- Show this screen.
"""
