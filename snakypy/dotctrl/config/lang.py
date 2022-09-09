from snakypy.dotctrl import __info__
from snakypy.dotctrl.utils.colors import Colors

c: Colors = Colors()

# Strucuture: "type:code": "text"

LANG: dict = {
    "pt_BR": {},
    "en_US": {
        "word:01": "Arquivo(s)",
        "word:03": "Elemento(s)",
        "word:04": "Diretório(s)",
        "word:05": "Unidade(s)",
        "word:06": "Ativado",
        "word:07": "Desativado",
        "word:08": "Sim",
        "word:09": "Não",
        "word:10": "Arquivo",
        "word:11": "Diretório",
        "word:12": "",
        "word:13": "Total",
        "word:14": "Pasta",
        "word:15": "Resultado",
        "msg:01": "Oferecido por:",
        "msg:02": "Repositório está vazio. Sem elementos.",
        "msg:03": (
            f"Os elementos abaixo são encontrados no diretorio do {__info__['name']}. "
            f"""{c.blue('(Digite "q" para sair)', c.YELLOW)}"""
        ),
        "msg:04": "[Code:04] Elemento não encontrado no repositório.",
        "msg:05": "[Code:05] Elemento não linkado. Revise o mesmo no repositório:",
        "msg:06": "O repositório já está definido em",
        "msg:07": f"{__info__['name']} já está configurado no diretório: ",
        "msg:08": (
            "Você deve ter permissão SUDO em sua máquina para prosseguir com esta etapa e criar "
            f"um repositório automático com {__info__['name']}. Você pode abordar a operação por "
            "pressionando Ctrl + C.\n"
            f"NOTA: O diretório {__info__['name']} será criado em: "
        ),
        "msg:09": "[ Digite a senha para sudo ]",
        "msg:10": f"Inicializado {__info__['name']} no repositório: ",
        "msg:11": f"[Code:11] O elemento não existe no repositório do {__info__['name']} para ser linkado.",
        "msg:12": "Elemento desvinculado com sucesso!",
        "msg:13": "Tipo: | Elemento ",
        "msg:14": "Nada a ligar, em massa.",
        "msg:15": "Elemento(s) vinculado(s) com sucesso!",
        "msg:16": "Nada foi puxado. Elemento inexistente.",
        "msg:17": "Nada para puxar, em massa.",
        "msg:18": "Elemento(s) puxado(s) com sucesso!",
        "msg:19": "Repositório vazio. Nada a ligar.",
        "msg:20": "Não linkado!",
        "msg:21": "Parabéns! Todos os elementos estão ligados.",
        "msg:22": (
            "Os elementos abaixo NÃO estão vinculados! "
            f'Use "{c.cyan("dotctrl link", c.YELLOW)}" para vinculá-los.'
        ),
        "msg:23": f"Informações do repositório {__info__['name']}:",
        "msg:24": "O repositório está vazio de registro. Sem elementos.",
        "msg:25": (
            f'Lista do(s) elemento(s) do repositório {__info__["name"]}. '
            f"""{c.blue('(Digite "q" para sair)', c.YELLOW)}"""
        ),
        "msg:26": "Tipo:   Elemento  <-  Link simbólico\n",
        "msg:27": (
            "[Code:27] Existe um arquivo no local de origem. "
            "Caso queira prosseguir e substituir este elemento encontrado "
            f"pelo elemento do repositório {__info__['name']}, use a opção --force (--f).\n"
        ),
        "msg:28": (
            "O repositório não está criado. "
            f"Use \"{__info__['pkg_name']} init [--auto] [--git]\". Aborted"
        ),
        "msg:29": "[Code:29] Elemento não encontrado.",
        "msg:30": "Nada para desvinculado, em massa.",
        "msg:31": "Links massivamente desvinculados com sucesso!",
        "msg:32": "[Code:32] Arquivo de configuração não encontrado",  # not used
        "msg:33": "[Code:33] Ocorreu um erro ao ler o arquivo de configuração.",  # not used
        "msg:34": "Provavelmente o repositório não foi criado. Use: dotctrl init [--auto | --git ]",  # not used
        "msg:35": "Limpeza concluida!",
        "msg:36": "Nada a limpar!",
        "msg:37": (
            f"[Code:37] Arquivos com o mesmo nome foram encontrados no repositório {__info__['name']} e no local de origem."
            f"Para substituir os do repositorio do {__info__['name']}, use a opção --force (--f)."
        ),
        "msg:38": (
            "[Code:38] Elemento não encontrado no repositório para restaurar.\n"
            "Isso pode ser causado porque o arquivo de configuração está desatualizado.\n"
            "Antes de prosseguir com a restauração, use o comando: "
            "'dotctrl config --autoclean' para atualizar. "
        ),
        "msg:39": (
            f"[Code:39] O {__info__['name']} encontrou um link simbólico de um elemento que não é "
            f"vinculado com o repositório do {__info__['name']}.\n"
            "Caso queira prosseguir e substituir este link simbólico encontrado "
            f"pelo elemento do repositório {__info__['name']}, use a opção --force (--f).\n"
            f'{c.magenta("Nota", c.YELLOW)}: Se usar a opção {c.cyan("--force (--f)", c.YELLOW)}, este link simbólico '
            "encontrado será removido (e demais). "
            "Recomendamos que, averigue este link simbólico antes de prosseguir com a opção --force (--f).\n\n"
            "Link simbólico encontrado: "
        ),
        "msg:40": "Repositório vazio. Nada para restaurar.",
        "msg:41": (
            "Está opção ira fazer a restauração em massa de todos elementos "
            "do repositório do Dotctrl para o local original.\n   Deseja continuar?\n"
        ),
        "msg:42": "Cancelado pelo usuário.",
        "msg:43": "[Code:43] Opção inválida!",
        "msg:44": (
            f"[Code:44] O {__info__['name']} ENCONTROU um elemento no local de origem com mesmo nome do "
            f"repositório do {__info__['name']}, e isso impediu de prosseguir com a restauração.\n"
            f"Caso queira substituí-lo pelo elemento do repositório {__info__['name']}, "
            "execute este comando novamente com a opção --force (--f).\n"
            f"{c.magenta('Nota', c.YELLOW)}: Se usar a opção {c.cyan('--force (--f)', c.YELLOW)}, este elemento "
            "encontrado (e demais) será(ão) removido(s). "
            "Recomendamos que, averigue este (e demais) elemento(s) antes de prosseguir com a opção --force (--f).\n\n"
            "Elemento encontrado: "
        ),
        "msg:45": "Operação abordada!",
        "msg:46": "Restauração completa!",
        "msg:47": f"Escolha um idioma para o {__info__['name']}:",
        "msg:48": "Idioma alterado com sucesso! Alterado para:",
        "msg:49": "[Code:49] Erro na autenticação da senha.",
    },
}
