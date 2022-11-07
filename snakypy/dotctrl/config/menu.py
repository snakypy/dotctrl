"""Module menu"""

from os.path import exists
from re import sub
from typing import Any

from docopt import docopt
from snakypy.helpers import FG
from snakypy.helpers.ansi import NONE

from snakypy.dotctrl import __info__
from snakypy.dotctrl.config.base import Base
from snakypy.dotctrl.utils import get_key

EXE = __info__["executable"]

EN_US: str = f"""
{__info__['name']} - Managing your dotfiles in $HOME on Linux or macOS.

USAGE:
    {EXE} init [--auto] [--git]
    {EXE} pull [--e=<object> | --element=<object>] [--f | --force]
    {EXE} link [--e=<object> | --element=<object>] [--f | --force]
    {EXE} unlink [--e=<object> | --element=<object>] [--f | --force]
    {EXE} restore [--e=<object> | --element=<object>] [--f | --force]
    {EXE} repo (--check | --ls | --info)
    {EXE} find (--name=<object>)
    {EXE} config (--open | --view | --lang | --autoclean)
    {EXE} --help
    {EXE} --version
    {EXE} --credits

ARGUMENTS:
    #init# ----------- Creates the dotfiles repository.
    #find# ----------- Find some object in the Dotctrl repository.
    #pull# ----------- Pulls the elements from the source
                     location on the machine to the repository.
    #link# ----------- Links the repository's elements to the source location
                     on the machine.
    #repo# ----------- Show {__info__["name"]} repository information.
    #unlink# --------- Unlink the elements from the repository
                     with the original location on the machine.
    #config# --------- Manager the configuration file.
    #restore# -------- Moves elements from the repository to the default source
                     location.

OPTIONS:
    #--check# --------------------- Checks whether the elements in the
                                  repository are linked to the place of origin
                                  or not.
    #--e or --element <object># ---- Receives an object without its absolute
                                  path, just the relative one.
    #--open# ---------------------- Open a file in edit mode.
    #--view# ---------------------- View the contents of a file in the terminal
    #--git# ----------------------- Create a Git repository.
    #--auto# ---------------------- Creates the {__info__["name"]} repository
                                  automatically in the users directory.
                                  On Linux it will create in "/home", on macOS
                                  in "/Users".
                                  (You must have SUDO permission).
    #--info# ---------------------- Shows detailed information for the
                                  {__info__["name"]} repository.
    #--ls# ------------------------ List all files and folders in the
                                  {__info__["name"]} repository.
    #--lang# ---------------------- Change the language of {__info__["name"]}.
    #--name <object># ------------- Receives the name of an object, it can be a
                                  folder or a file.
    #--f or --force# --------------- Complete the command regardless of whether
                                  or not files exist.
                                  ATTENTION! Using this option will replace
                                  existing files.
    #--autoclean# ----------------- Clear the {__info__["name"]} registry, if
                                  there is no element in the repository.
    #--version# ------------------- Show version.
    #--credits# ------------------- Show credits.
    #--help# ---------------------- Show this screen.
"""

PT_BR = f"""
{__info__['name']} - Gerenciando seus dotfiles do HOME no Linux ou macOS.

USAGE:
    {EXE} init [--auto] [--git]
    {EXE} pull [--e=<object> | --element=<object>] [--f | --force]
    {EXE} link [--e=<object> | --element=<object>] [--f | --force]
    {EXE} unlink [--e=<object> | --element=<object>] [--f | --force]
    {EXE} restore [--e=<object> | --element=<object>] [--f | --force]
    {EXE} repo (--check | --ls | --info)
    {EXE} find (--name=<object>)
    {EXE} config (--open | --view | --lang | --autoclean)
    {EXE} --help
    {EXE} --version
    {EXE} --credits

ARGUMENTOS:
    #init# ----------- Cria o repositório dotfiles.
    #find# ----------- Encontre algum objeto no repositório Dotctrl.
    #pull# ----------- Pega elementos do local de origem na
                     máquina para o repositório.
    #link# ----------- Vincula os elementos do repositório ao local de origem
                     na máquina.
    #repo# ----------- Mostrar informações do repositório {__info__["name"]}.
    #unlink# --------- Desvincula os elementos do repositório com o local
                     original na máquina.
    #config# --------- Gerencia o arquivo de configuração.
    #restore# -------- Move elementos do repositório para o local de origem
                     padrão.

OPÇÕES:
    #--check# --------------------- Verifica se os elementos no repositório
                                  estão vinculados a o local de origem ou não.
    #--e or --element <object># ---- Recebe um objeto sem seu caminho absoluto,
                                  apenas o relativo.
    #--open# ---------------------- Abra um arquivo no modo de edição.
    #--view# ---------------------- Visualize o conteúdo de um arquivo no
                                  terminal.
    #--git# ----------------------- Crie um repositório Git.
    #--auto# ---------------------- Cria o repositório {__info__["name"]}
                                  automaticamente no diretório do usuário. No
                                  Linux, ele criará em "/home", no macOS em
                                  "/Users".
                                  (Está opção exige permissão de SUDO).
    #--info# ---------------------- Mostra informações detalhadas do
                                  repositório {__info__["name"]}.
    #--ls# ------------------------ Liste todos os arquivos e pastas no
                                  repositório {__info__["name"]}.
    #--lang# ---------------------- Altere o idioma do {__info__["name"]}.
    #--name <object># ------------- Recebe o nome de um objeto, pode ser uma
                                  pasta ou um arquivo.
    #--f or --force# --------------- Conclua o comando independentemente de
                                  existirem ou não arquivos.
                                  ATENÇÃO! O uso desta opção substituirá os
                                  arquivos existentes.
    #--autoclean# ----------------- Limpe o registro dos elementos no
                                  {__info__["name"]} (se não houver nenhum
                                  elemento no repositório).
    #--version# ------------------- Mostra a versão.
    #--credits# ------------------- Mostra os créditos.
    #--help# ---------------------- Mostre esta tela.
"""


def colorize(texts: list, color: str, keys: list) -> list:
    ret = []
    for key in keys:
        for text in texts:
            key = sub(
                text,
                f'{color}{text.replace("#", "")}{NONE}',
                key,
            )
            ret.append(key)

    return ret


TEXTS_CYAN = [
    "#init#",
    "#find#",
    "#pull#",
    "#link#",
    "#repo#",
    "#unlink#",
    "#config#",
    "#restore#",
]

COLORIZE = colorize(TEXTS_CYAN, FG().CYAN, [EN_US, PT_BR])

EN_US = COLORIZE[len(TEXTS_CYAN) - 1]
PT_BR = COLORIZE[len(TEXTS_CYAN) - 1]

TEXTS_BLUE = [
    "#--check#",
    "#--e or --element <object>#",
    "#--open#",
    "#--view#",
    "#--git#",
    "#--name <object>#",
    "#--auto#",
    "#--info#",
    "#--ls#",
    "#--lang#",
    "#--f or --force#",
    "#--autoclean#",
    "#--version#",
    "#--credits#",
    "#--help#",
]

COLORIZE = colorize(TEXTS_BLUE, FG().BLUE, [EN_US, PT_BR])

EN_US = COLORIZE[len(TEXTS_BLUE) - 1]
PT_BR = COLORIZE[len(TEXTS_BLUE) - 1]


class Menu(Base):
    def __init__(self, root: str, home: str) -> None:
        Base.__init__(self, root, home)

    @staticmethod
    def languages() -> dict:
        return {"pt_BR": PT_BR, "en_US": EN_US}

    @property
    def menu(self) -> str:

        if exists(self.config_path):
            lang_current: str = get_key(
                self.parsed, "dotctrl", "config", "language"
            )

            if not lang_current or lang_current not in self.languages().keys():
                return self.languages()["en_US"]
            return self.languages()[lang_current]
        else:
            return self.languages()["en_US"]

    def args(self, argv: Any = None) -> dict:
        """Function to return the option menu arguments."""

        formatted_version: str = (
            f"{__info__['name']} version: "
            f"{FG().CYAN}{__info__['version']}{NONE}"
        )

        data: dict = docopt(self.menu, argv=argv, version=formatted_version)

        return data
