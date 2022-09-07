from snakypy.dotctrl import __info__
from snakypy.dotctrl.utils.colors import Colors

c = Colors()

LANG = {
    "en_US": {
        "cod:w01": "Arquivo(s)",
        "cod:w03": "Elemento(s)",
        "cod:w04": "Diretório(s)",
        "cod:w05": "Unidade(s)",
        "cod:w06": "Ativado",
        "cod:w07": "Desativado",
        "cod:w08": "Sim",
        "cod:w09": "Não",
        "cod:w10": "Arquivo",
        "cod:w11": "Diretório",
        "cod:w12": "",
        "cod:w13": "Total",
        "cod:w14": "Pasta",
        "cod:w15": "Resultado",
        "cod:01": "Oferecido por:",
        "cod:02": "Repositório está vazio. Sem elementos.",
        "cod:03": (
            f"Os elementos abaixo são encontrados no diretorio do {__info__['name']}. "
            f"""{c.blue('(Digite "q" para sair)', c.YELLOW)}"""
        ),
        "cod:04": "",
        "cod:05": "[Cod:05] Elemento não linkado. Revise o mesmo no repositório:",
        "cod:06": "O repositório já está definido em: ",
        "cod:07": f"{__info__['name']} já está configurado no diretório: ",
        "cod:08": (
            "Você deve ter permissão SUDO em sua máquina para prosseguir com esta etapa e criar "
            f"um repositório automático com {__info__['name']}. Você pode abordar a operação por "
            "pressionando Ctrl + C.\n"
            f"NOTA: O diretório {__info__['name']} será criado em: "
        ),
        "cod:09": "[ Digite a senha para sudo ]",
        "cod:10": f"Inicializado {__info__['name']} no repositório: ",
        "cod:11": f"[Cod:11] O elemento não existe no repositório do {__info__['name']} para ser linkado.",
        "cod:12": "Elemento desvinculado com sucesso!",
        "cod:13": "Tipo: | Elemento ",
        "cod:14": "Nada a ligar, em massa.",
        "cod:15": "Elemento(s) vinculado(s) com sucesso!",
        "cod:16": "Nada foi puxado. Elemento inexistente.",
        "cod:17": "Nada para puxar, em massa.",
        "cod:18": "Elemento(s) puxado(s) com sucesso!",
        "cod:19": "Repositório vazio. Nada a ligar.",
        "cod:20": "Não linkado!",
        "cod:21": "Congratulations! All elements are linked.",
        "cod:22": (
            "Os elementos abaixo NÃO estão vinculados! "
            f'Use "{c.cyan("dotctrl link", c.YELLOW)}" para vinculá-los.'
        ),
        "cod:23": f"Informações do repositório {__info__['name']}:",
        "cod:24": "O repositório está vazio de registro. Sem elementos.",
        "cod:25": (
            f'Lista do(s) elemento(s) do repositório {__info__["name"]}. '
            f"""{c.blue('(Digite "q" para sair)', c.YELLOW)}"""
        ),
        "cod:26": "Tipo:   Elemento  <-  Link simbólico\n",
        "cod:27": (
            "[Cod:27] Existe um arquivo no local de origem. "
            "Caso queira prosseguir e substituir este elemento encontrado "
            f"pelo elemento do repositório {__info__['name']}, use a opção --force (--f).\n"
        ),
        "cod:28": "",
        "cod:29": "[Cod:29] Elemento não encontrado.",
        "cod:30": "Nada para desvinculado, em massa.",
        "cod:31": "Links massivamente desvinculados com sucesso!",
        "cod:32": "[Cod:32] Arquivo de configuração não encontrado",
        "cod:33": "[Cod:33] Ocorreu um erro ao ler o arquivo de configuração.",
        "cod:34": "Provavelmente o repositório não foi criado. Use: dotctrl init [--auto | --git ]",
        "cod:35": "Limpeza concluida!",
        "cod:36": "Nada a limpar!",
        "cod:37": (
            f"[Cod:37] Arquivos com o mesmo nome foram encontrados no repositório {__info__['name']} e no local de origem."
            f"Para substituir os do repositorio do {__info__['name']}, use a opção --force (--f)."
        ),
        "cod:38": (
            "[Cod:38] Elemento não encontrado no repositório para restaurar.\n"
            "Isso pode ser causado porque o arquivo de configuração está desatualizado.\n"
            "Antes de prosseguir com a restauração, use o comando: "
            "'dotctrl config --autoclean' para atualizar. "
        ),
        "cod:39": (
            f"[Cod:39] O {__info__['name']} encontrou um link simbólico de um elemento que não é "
            f"vinculado com o repositório do {__info__['name']}.\n"
            "Caso queira prosseguir e substituir este link simbólico encontrado "
            f"pelo elemento do repositório {__info__['name']}, use a opção --force (--f).\n"
            f'{c.magenta("Nota", c.YELLOW)}: Se usar a opção {c.cyan("--force (--f)", c.YELLOW)}, este link simbólico '
            "encontrado será removido (e demais). "
            "Recomendamos que, averigue este link simbólico antes de prosseguir com a opção --force (--f).\n\n"
            "Link simbólico encontrado: "
        ),
        "cod:40": "Repositório vazio. Nada para restaurar.",
        "cod:41": (
            "Está opção ira fazer a restauração em massa de todos elementos "
            "do repositório do Dotctrl para o local original.\n   Deseja continuar?\n"
        ),
        "cod:42": "Cancelado pelo usuário.",
        "cod:43": "[cod:43] Opção inválida!",
        "cod:44": (
            f"[cod:44] O {__info__['name']} ENCONTROU um elemento no local de origem com mesmo nome do "
            f"repositório do {__info__['name']}, e isso impediu de prosseguir com a restauração.\n"
            f"Caso queira substituí-lo pelo elemento do repositório {__info__['name']}, "
            "execute este comando novamente com a opção --force (--f).\n"
            f"{c.magenta('Nota', c.YELLOW)}: Se usar a opção {c.cyan('--force (--f)', c.YELLOW)}, este elemento "
            "encontrado (e demais) será(ão) removido(s). "
            "Recomendamos que, averigue este (e demais) elemento(s) antes de prosseguir com a opção --force (--f).\n\n"
            "Elemento encontrado: "
        ),
        "cod:45": "Operação abordada!",
        "cod:46": "Restauração completa!",
        "cod:47": f"Escolha um idioma para o {__info__['name']}:",
        "cod:48": "Idioma alterado com sucesso!",
        "cod:49": "[cod:49] Erro na autenticação da senha.",
    },
    "pt_BR": {
        "cod:w01": "Arquivo(s)",
        "cod:w03": "Elemento(s)",
        "cod:w04": "Diretório(s)",
        "cod:w05": "Unidade(s)",
        "cod:w06": "Ativado",
        "cod:w07": "Desativado",
        "cod:w08": "Sim",
        "cod:w09": "Não",
        "cod:w10": "Arquivo",
        "cod:w11": "Diretório",
        "cod:w12": "",
        "cod:w13": "Total",
        "cod:w14": "Pasta",
        "cod:w15": "Resultado",
        "cod:01": "Oferecido por:",
        "cod:02": "Repositório está vazio. Sem elementos.",
        "cod:03": (
            f"Os elementos abaixo são encontrados no diretorio do {__info__['name']}. "
            f"""{c.blue('(Digite "q" para sair)', c.YELLOW)}"""
        ),
        "cod:04": "",
        "cod:05": "[Cod:05] Elemento não linkado. Revise o mesmo no repositório:",
        "cod:06": "O repositório já está definido em",
        "cod:07": f"{__info__['name']} já está configurado no diretório: ",
        "cod:08": (
            "Você deve ter permissão SUDO em sua máquina para prosseguir com esta etapa e criar "
            f"um repositório automático com {__info__['name']}. Você pode abordar a operação por "
            "pressionando Ctrl + C.\n"
            f"NOTA: O diretório {__info__['name']} será criado em: "
        ),
        "cod:09": "[ Digite a senha para sudo ]",
        "cod:10": f"Inicializado {__info__['name']} no repositório: ",
        "cod:11": f"[Cod:11] O elemento não existe no repositório do {__info__['name']} para ser linkado.",
        "cod:12": "Elemento desvinculado com sucesso!",
        "cod:13": "Tipo: | Elemento ",
        "cod:14": "Nada a ligar, em massa.",
        "cod:15": "Elemento(s) vinculado(s) com sucesso!",
        "cod:16": "Nada foi puxado. Elemento inexistente.",
        "cod:17": "Nada para puxar, em massa.",
        "cod:18": "Elemento(s) puxado(s) com sucesso!",
        "cod:19": "Repositório vazio. Nada a ligar.",
        "cod:20": "Não linkado!",
        "cod:21": "Parabéns! Todos os elementos estão ligados.",
        "cod:22": (
            "Os elementos abaixo NÃO estão vinculados! "
            f'Use "{c.cyan("dotctrl link", c.YELLOW)}" para vinculá-los.'
        ),
        "cod:23": f"Informações do repositório {__info__['name']}:",
        "cod:24": "O repositório está vazio de registro. Sem elementos.",
        "cod:25": (
            f'Lista do(s) elemento(s) do repositório {__info__["name"]}. '
            f"""{c.blue('(Digite "q" para sair)', c.YELLOW)}"""
        ),
        "cod:26": "Tipo:   Elemento  <-  Link simbólico\n",
        "cod:27": (
            "[Cod:27] Existe um arquivo no local de origem. "
            "Caso queira prosseguir e substituir este elemento encontrado "
            f"pelo elemento do repositório {__info__['name']}, use a opção --force (--f).\n"
        ),
        "cod:28": "",
        "cod:29": "[Cod:29] Elemento não encontrado.",
        "cod:30": "Nada para desvinculado, em massa.",
        "cod:31": "Links massivamente desvinculados com sucesso!",
        "cod:32": "[Cod:32] Arquivo de configuração não encontrado",
        "cod:33": "[Cod:33] Ocorreu um erro ao ler o arquivo de configuração.",
        "cod:34": "Provavelmente o repositório não foi criado. Use: dotctrl init [--auto | --git ]",
        "cod:35": "Limpeza concluida!",
        "cod:36": "Nada a limpar!",
        "cod:37": (
            f"[Cod:37] Arquivos com o mesmo nome foram encontrados no repositório {__info__['name']} e no local de origem."
            f"Para substituir os do repositorio do {__info__['name']}, use a opção --force (--f)."
        ),
        "cod:38": (
            "[Cod:38] Elemento não encontrado no repositório para restaurar.\n"
            "Isso pode ser causado porque o arquivo de configuração está desatualizado.\n"
            "Antes de prosseguir com a restauração, use o comando: "
            "'dotctrl config --autoclean' para atualizar. "
        ),
        "cod:39": (
            f"[Cod:39] O {__info__['name']} encontrou um link simbólico de um elemento que não é "
            f"vinculado com o repositório do {__info__['name']}.\n"
            "Caso queira prosseguir e substituir este link simbólico encontrado "
            f"pelo elemento do repositório {__info__['name']}, use a opção --force (--f).\n"
            f'{c.magenta("Nota", c.YELLOW)}: Se usar a opção {c.cyan("--force (--f)", c.YELLOW)}, este link simbólico '
            "encontrado será removido (e demais). "
            "Recomendamos que, averigue este link simbólico antes de prosseguir com a opção --force (--f).\n\n"
            "Link simbólico encontrado: "
        ),
        "cod:40": "Repositório vazio. Nada para restaurar.",
        "cod:41": (
            "Está opção ira fazer a restauração em massa de todos elementos "
            "do repositório do Dotctrl para o local original.\n   Deseja continuar?\n"
        ),
        "cod:42": "Cancelado pelo usuário.",
        "cod:43": "[cod:43] Opção inválida!",
        "cod:44": (
            f"[cod:44] O {__info__['name']} ENCONTROU um elemento no local de origem com mesmo nome do "
            f"repositório do {__info__['name']}, e isso impediu de prosseguir com a restauração.\n"
            f"Caso queira substituí-lo pelo elemento do repositório {__info__['name']}, "
            "execute este comando novamente com a opção --force (--f).\n"
            f"{c.magenta('Nota', c.YELLOW)}: Se usar a opção {c.cyan('--force (--f)', c.YELLOW)}, este elemento "
            "encontrado (e demais) será(ão) removido(s). "
            "Recomendamos que, averigue este (e demais) elemento(s) antes de prosseguir com a opção --force (--f).\n\n"
            "Elemento encontrado: "
        ),
        "cod:45": "Operação abordada!",
        "cod:46": "Restauração completa!",
        "cod:47": f"Escolha um idioma para o {__info__['name']}:",
        "cod:48": "Idioma alterado com sucesso!",
        "cod:49": "[cod:49] Erro na autenticação da senha.",
    },
}
