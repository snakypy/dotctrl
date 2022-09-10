from snakypy.dotctrl import __info__
from snakypy.dotctrl.utils.colors import Colors

c: Colors = Colors()

# Strucuture: "type:code": "text"

LANG: dict = {
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
        "word:12": "",  # empty
        "word:13": "Total",
        "word:14": "Pasta",
        "word:15": "Resultado",
        "msg:01": "Oferecido por:",
        "msg:02": "Repositório está vazio. Sem elementos.",
        "msg:03": (
            f"Os elementos abaixo são encontrados no diretorio do {__info__['name']}. "
            f"""{c.blue('(Digite "q" para sair)', c.YELLOW)}\n"""
        ),
        "msg:04": f"{c.cyan('[Code:04]', c.YELLOW)} Elemento não encontrado no repositório.",
        "msg:05": f"{c.cyan('[Code:05]', c.YELLOW)} Elemento não linkado. Revise o mesmo no repositório:",
        "msg:06": "O repositório já está definido em",
        "msg:07": f"{__info__['name']} já está configurado no diretório: ",
        "msg:08": (
            "AVISO!\nVocê deve ter permissão SUDO em sua máquina para prosseguir com esta etapa e criar\n"
            f"um repositório automático com {__info__['name']}.\n"
            f"Você pode abordar a operação pressionando {c.cyan('Ctrl + C', c.YELLOW)}.\n\n"
            f"{c.magenta('NOTA', c.YELLOW)}: O diretório {__info__['name']} será criado em:"
        ),
        "msg:09": "[ Digite a senha para sudo ]",
        "msg:10": f"Inicializado {__info__['name']} no repositório: ",
        "msg:11": (
            f"{c.cyan('[Code:11]', c.YELLOW)} O elemento não existe no repositório do {__info__['name']} "
            "para ser linkado."
        ),
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
            f"{c.cyan('[Code:27]', c.YELLOW)} Existe um arquivo no local de origem. "
            "Caso queira prosseguir e substituir este elemento encontrado "
            f"pelo elemento do repositório {__info__['name']}, use a opção --force (--f).\n"
        ),
        "msg:28": (
            "O repositório não está criado. "
            f"Use \"{__info__['pkg_name']} init [--auto] [--git]\". Aborted"
        ),
        "msg:29": f"{c.cyan('[Code:29]', c.RED)} Elemento não encontrado.",
        "msg:30": "Nada para desvinculado, em massa.",
        "msg:31": "Links massivamente desvinculados com sucesso!",
        "msg:32": "",  # empty
        "msg:33": "",  # empty
        "msg:34": "",  # empty
        "msg:35": "Limpeza concluida!",
        "msg:36": "Nada a limpar!",
        "msg:37": (
            f"{c.cyan('[Code:37]', c.YELLOW)} Elementos com o mesmo nome foram encontrados no repositório "
            f"{__info__['name']} e no local de origem. Esses elementos não tem vinculo com o repositório do "
            f"{__info__['name']}.\n"
            f"Para substituir os do repositorio do {__info__['name']}, use a opção {c.cyan('--force (--f)', c.YELLOW)}."
        ),
        "msg:38": (
            f"{c.cyan('[Code:38]', c.YELLOW)} Foi detectado no arquivo de configuração do {__info__['name']} que "
            "algum elemento não existe no repositório para restaurar.\n"
            "Isso pode ser causado porque o arquivo de configuração está desatualizado.\n"
            "Antes de prosseguir com a restauração, use o comando: "
            f'"{c.cyan("dotctrl config --autoclean", c.YELLOW)}" para atualizar. '
        ),
        "msg:39": (
            f"{c.cyan('[Code:39]', c.YELLOW)} O {__info__['name']} encontrou um link simbólico de um elemento que não é "
            f"vinculado com o repositório do {__info__['name']}.\n"
            "Caso queira prosseguir e substituir este link simbólico (e demais) encontrado "
            f"pelo elemento do repositório {__info__['name']}, use a opção --force (--f).\n"
            f'{c.magenta("Nota", c.YELLOW)}: Se usar a opção {c.cyan("--force (--f)", c.YELLOW)}, este link simbólico '
            "encontrado será removido. "
            "Recomendamos que, averigue este link simbólico antes de prosseguir com a opção "
            f"{c.cyan('--force (--f)', c.YELLOW)}.\n\n"
            f"{c.magenta('Link simbólico encontrado')}: "
        ),
        "msg:40": "Repositório vazio. Nada para restaurar.",
        "msg:41": (
            "Está opção ira fazer a restauração em massa de todos elementos "
            f"do repositório do {__info__['name']} para o local original.\n   Deseja continuar?\n"
        ),
        "msg:42": "Cancelado pelo usuário.",
        "msg:43": f"{c.cyan('[Code:43]', c.RED)} Opção inválida!",
        "msg:44": (
            f"{c.cyan('[Code:44]', c.YELLOW)} O {__info__['name']} ENCONTROU um elemento no local de origem com "
            f"mesmo nome do repositório do {__info__['name']}, e isso impediu de prosseguir com a restauração.\n"
            f"Caso queira substituí-lo pelo elemento do repositório {__info__['name']}, "
            f"execute este comando novamente com a opção {c.cyan('--force (--f)', c.YELLOW)}.\n"
            f"{c.magenta('Nota', c.YELLOW)}: Se usar a opção {c.cyan('--force (--f)', c.YELLOW)}, este elemento "
            "encontrado (e demais) será(ão) removido(s). "
            "Recomendamos que, averigue este (e demais) elemento(s) antes de prosseguir com a opção --force (--f).\n\n"
            "Elemento encontrado: "
        ),
        "msg:45": "Operação abordada!",
        "msg:46": "Restauração completa!",
        "msg:47": f"Escolha um idioma para o {__info__['name']}:",
        "msg:48": "Idioma alterado com sucesso! Alterado para:",
        "msg:49": f"{c.cyan('[Code:49]', c.RED)} Erro na autenticação da senha.",
    },
}
