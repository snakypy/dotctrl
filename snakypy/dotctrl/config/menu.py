"""Module menu"""

from os.path import exists
from typing import Any

from docopt import docopt
from snakypy.helpers import FG
from snakypy.helpers.ansi import NONE

from snakypy.dotctrl import __info__
from snakypy.dotctrl.config.base import Base
from snakypy.dotctrl.utils import get_key

EN_US: str = f"""
{__info__['name']} - Managing your dotfiles in $HOME on Linux or macOS.

USAGE:
    {__info__['executable']} init [--auto] [--git]
    {__info__['executable']} pull [--e=<object> | --element=<object>] [--f | --force]
    {__info__['executable']} link [--e=<object> | --element=<object>] [--f | --force]
    {__info__['executable']} unlink [--e=<object> | --element=<object>] [--f | --force]
    {__info__['executable']} restore [--e=<object> | --element=<object>] [--f | --force]
    {__info__['executable']} repo (--check | --ls | --info)
    {__info__['executable']} find (--name=<object>)
    {__info__['executable']} config (--open | --view | --lang | --autoclean)
    {__info__['executable']} --help
    {__info__['executable']} --version
    {__info__['executable']} --credits

ARGUMENTS:
    {FG().CYAN}init{NONE} ----------- Creates the dotfiles repository.
    {FG().CYAN}find{NONE} ----------- Find some object in the Dotctrl repository.
    {FG().CYAN}pull{NONE} ----------- Pulls the elements from the source location on the
                     machine to the repository.
    {FG().CYAN}link{NONE} ----------- Links the repository's elements to the source location
                     on the machine.
    {FG().CYAN}repo{NONE} ----------- Show {__info__["name"]} repository information.
    {FG().CYAN}unlink{NONE} --------- Unlink the elements from the repository with the original location
                     on the machine.
    {FG().CYAN}config{NONE} --------- Manager the configuration file.
    {FG().CYAN}restore{NONE} -------- Moves elements from the repository to the default source location.

OPTIONS:
    {FG().BLUE}--check{NONE} --------------------- Checks whether the elements in the repository are linked to
                                  the place of origin or not.
    {FG().BLUE}--e | --element <object>{NONE} ---- Receives an object without its absolute path, just the relative one.
    {FG().BLUE}--open{NONE} ---------------------- Open a file in edit mode.
    {FG().BLUE}--view{NONE} ---------------------- View the contents of a file in the terminal.
    {FG().BLUE}--git{NONE} ----------------------- Create a Git repository.
    {FG().BLUE}--auto{NONE} ---------------------- Creates the {__info__["name"]} repository automatically in the users
                                  directory. On Linux it will create in "/home", on macOS in "/Users".
                                  (You must have SUDO permission).
    {FG().BLUE}--info{NONE} ---------------------- Shows detailed information for the {__info__["name"]} repository.
    {FG().BLUE}--ls{NONE} ------------------------ List all files and folders in the {__info__["name"]} repository.
    {FG().BLUE}--lang{NONE} ---------------------- Change the language of {__info__["name"]}.
    {FG().BLUE}--name <object>{NONE} ------------- Receives the name of an object, it can be a folder or a file.
    {FG().BLUE}--f | --force{NONE} --------------- Complete the command regardless of whether or not files exist.
                                  ATTENTION! Using this option will replace existing files.
    {FG().BLUE}--autoclean{NONE} ----------------- Clear the {__info__["name"]} registry, if there is no element in the
                                  repository.
    {FG().BLUE}--version{NONE} ------------------- Show version.
    {FG().BLUE}--credits{NONE} ------------------- Show credits.
    {FG().BLUE}--help{NONE} ---------------------- Show this screen.
"""

PT_BR = f"""
{__info__['name']} - Gerenciando seus dotfiles do HOME no Linux ou macOS.

USAGE:
    {__info__['executable']} init [--auto] [--git]
    {__info__['executable']} pull [--e=<object> | --element=<object>] [--f | --force]
    {__info__['executable']} link [--e=<object> | --element=<object>] [--f | --force]
    {__info__['executable']} unlink [--e=<object> | --element=<object>] [--f | --force]
    {__info__['executable']} restore [--e=<object> | --element=<object>] [--f | --force]
    {__info__['executable']} repo (--check | --ls | --info)
    {__info__['executable']} find (--name=<object>)
    {__info__['executable']} config (--open | --view | --lang | --autoclean)
    {__info__['executable']} --help
    {__info__['executable']} --version
    {__info__['executable']} --credits

ARGUMENTOS:
    {FG().CYAN}init{NONE} ----------- Cria o repositório dotfiles.
    {FG().CYAN}find{NONE} ----------- Encontre algum objeto no repositório Dotctrl.
    {FG().CYAN}pull{NONE} ----------- Pega elementos do local de origem na
                     máquina para o repositório.
    {FG().CYAN}link{NONE} ----------- Vincula os elementos do repositório ao local de origem
                     na máquina.
    {FG().CYAN}repo{NONE} ----------- Mostrar informações do repositório {__info__["name"]}.
    {FG().CYAN}unlink{NONE} --------- Desvincula os elementos do repositório com o local original
                     na máquina.
    {FG().CYAN}config{NONE} --------- Gerencia o arquivo de configuração.
    {FG().CYAN}restore{NONE} -------- Move elementos do repositório para o local de origem padrão.

OPÇÕES:
    {FG().BLUE}--check{NONE} --------------------- Verifica se os elementos no repositório estão vinculados a
                                  o local de origem ou não.
    {FG().BLUE}--e | --element <object>{NONE} ---- Recebe um objeto sem seu caminho absoluto, apenas o relativo.
    {FG().BLUE}--open{NONE} ---------------------- Abra um arquivo no modo de edição.
    {FG().BLUE}--view{NONE} ---------------------- Visualize o conteúdo de um arquivo no terminal.
    {FG().BLUE}--git{NONE} ----------------------- Crie um repositório Git.
    {FG().BLUE}--auto{NONE} ---------------------- Cria o repositório {__info__["name"]} automaticamente no diretório do
                                  usuário. No Linux, ele criará em "/home", no macOS em "/Users".
                                  (Está opção exige permissão de SUDO).
    {FG().BLUE}--info{NONE} ---------------------- Mostra informações detalhadas do repositório {__info__["name"]}.
    {FG().BLUE}--ls{NONE} ------------------------ Liste todos os arquivos e pastas no repositório {__info__["name"]}.
    {FG().BLUE}--lang{NONE} ---------------------- Altere o idioma do {__info__["name"]}.
    {FG().BLUE}--name <object>{NONE} ------------- Recebe o nome de um objeto, pode ser uma pasta ou um arquivo.
    {FG().BLUE}--f | --force{NONE} --------------- Conclua o comando independentemente de existirem ou não arquivos.
                                  ATENÇÃO! O uso desta opção substituirá os arquivos existentes.
    {FG().BLUE}--autoclean{NONE} ----------------- Limpe o registro dos elementos no {__info__["name"]} (se não houver
                                  nenhum elemento no repositório).
    {FG().BLUE}--version{NONE} ------------------- Mostra a versão.
    {FG().BLUE}--credits{NONE} ------------------- Mostra os créditos.
    {FG().BLUE}--help{NONE} ---------------------- Mostre esta tela.
"""


class Menu(Base):
    def __init__(self, root: str, home: str) -> None:
        Base.__init__(self, root, home)

    @staticmethod
    def languages() -> dict:
        return {"pt_BR": PT_BR, "en_US": EN_US}

    @property
    def menu(self) -> str:

        if exists(self.config_path):
            lang_current: str = get_key(self.parsed, "dotctrl", "config", "language")

            if not lang_current or lang_current not in self.languages().keys():
                return self.languages()["en_US"]
            return self.languages()[lang_current]
        else:
            return self.languages()["en_US"]

    def args(self, argv: Any = None) -> dict:
        """Function to return the option menu arguments."""

        formatted_version: str = (
            f"{__info__['name']} version: " f"{FG().CYAN}{__info__['version']}{NONE}"
        )

        data: dict = docopt(self.menu, argv=argv, version=formatted_version)

        return data
