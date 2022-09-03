from snakypy.dotctrl import __info__


LANG = {
    "en_US": {
        "words": (
            "File",
            "Files",
            "Path",
            "Element",
            "Elements",
            "Directory",
            "Directories",
            "Congratulations!",
            "Unit",
            "Active",
            "Disabled",
            "Yes",
            "No",
        ),
        "str:1": "Offered by:",
        "str:2": "Repository is empty. No elements.",
        "str:3": f"The elements below are found in the {__info__['name']} directory.",
        "str:4": '[ Result: ] (Type "q" to exit)',
        "str:6": "Repository is already defined in",
        "str:7": "is already configured in this directory",
        "str:8": f"""
        [ATTENTION!]

            You must have SUDO permission on your machine to proceed with this step and create
            an automatic repository with {__info__["name"]}. You can approach the operation by
            pressing Ctrl + C.

            NOTE: The {__info__['name']} directory will be created in:""",
        "str:9": "[ Enter password for sudo ]",
        "str:10": f"Initialized {__info__['name']} repository in",
        "str:11": f"""
        Link(s) was found, but maybe it can be linked from another location, but it's not
        from the {__info__['name']} repository.
        If you want to link to the {__info__['name']} repository, use the --force (--f) option.
        option to recreate.""",
        "str:12": "not linked.",
        "str:13": "Review the same in the repository.",
        "str:14": "Nothing to linked, en masse.",
        "str:15": "Element(s) linked successfully!",
        "str:16": "Nothing was pulled. Nonexistent element.",
        "str:17": "Nothing to pull, in droves.",
        "str:18": "Element(s) pulled successfully!",
        "str:19": "Empty repository. Nothing to link.",
        "str:20": "Not linked!",
        "str:21": "All elements are linked.",
        "str:22": "The elements below are NOT linked!",
        "str:23": f"{__info__['name']} Repository info:",
        "str:24": "The repository is empty of registration. No elements.",
        "str:25": (
            f'{__info__["name"]} repository element(s) list. (Type "q" to exit)'
        ),
        "str:26": "   Type  | Element  |  Simbolic Link\n",
        "str:27": f"""

        {__info__['name']} found links in the source location, but they are not
        from the {__info__['name']} repository. If you want to turn it off,
        use the --force (--f) option.""",
        "str:28": "not unlinked",
        "str:29": "Element not found.",
        "str:30": "Nothing to unlinked, en masse.",
        "str:31": "Massively unlinked links successfully!",
        "str:32": "Configuration file not found",
        "str:33": "An error occurred while reading the configuration file.",
        "str:34": "Probably the repository was not created. Use: dotctrl init [--auto | --git ]",
        "str:35": "Cleaning completed!",
        "str:36": "Nothing to clean!",
        "str:37": f"""

        Files with the same name were found in the {__info__['name']} repository and source location.
        To override those in the {__info__['name']} repository, use the --force (--f) option.
        """,
    },
    "pt_BR": {
        "words": (
            "Arquivo",
            "Arquivos",
            "Caminho",
            "Elemento",
            "Elementos",
            "Diretório",
            "Diretórios",
            "Parabéns!",
            "Unidade",
            "Ativo",
            "Desativado",
            "Sim",
            "Não",
        ),
        "str:1": "Oferecido por:",
        "str:2": "Repositório está vazio. Sem elementos.",
        "str:3": f"Os elementos abaixo são encontrados no diretorio do {__info__['name']}.",
        "str:4": '[ Resultado: ] (Digite "q" para sair)',
        "str:5": "Elemento:",
        "str:6": "O repositório já está definido em",
        "str:7": "já está configurado no diretório",
        "str:8": f"""
        [ATENÇÃO!]

            Você deve ter permissão SUDO em sua máquina para prosseguir com esta etapa e criar
            um repositório automático com {__info__["name"]}. Você pode abordar a operação por
            pressionando Ctrl + C.

            NOTA: O diretório {__info__['name']} será criado em:""",
        "str:9": "[ Digite a senha para sudo ]",
        "str:10": f"Inicializado {__info__['name']} no repositório",
        "str:11": f"""
        O(s) link(s) foi(m) encontrado(s), mas talvez possa ser vinculado de outro local, mas não é
        do repositório do {__info__['name']}.
        Se você deseja vincular do repositório do {__info__['name']}, use a opção --force (--f)
        para substituir o atual.""",
        "str:12": "não lincado.",
        "str:13": "Revise o mesmo no repositório.",
        "str:14": "Nada a ligar, em massa.",
        "str:15": "Elemento(s) vinculado(s) com sucesso!",
        "str:16": "Nada foi puxado. Elemento inexistente.",
        "str:17": "Nada para puxar, em massa.",
        "str:18": "Elemento(s) puxado(s) com sucesso!",
        "str:19": "Repositório vazio. Nada a ligar.",
        "str:20": "Não linkado!",
        "str:21": "Todos os elementos estão ligados.",
        "str:22": "Os elementos abaixo NÃO estão vinculados!",
        "str:23": f"Informações do repositório {__info__['name']}:",
        "str:24": "O repositório está vazio de registro. Sem elementos.",
        "str:25": (
            f'Lista do(s) elemento(s) do repositório {__info__["name"]}. '
            '(Digite "q" para sair)'
        ),
        "str:26": "   Tipo  | Elemento  |  Link simbólico\n",
        "str:27": f"""

        {__info__['name']} encontrou links no local de origem, mas eles não são
        do repositório {__info__['name']}. Se você quiser substitui-los use a opção --force (--f).""",
        "str:28": "não desvinculado.",
        "str:29": "Elemento não encontrado.",
        "str:30": "Nada para desvinculado, em massa.",
        "str:31": "Links massivamente desvinculados com sucesso!",
        "str:32": "Arquivo de configuração não encontrado",
        "str:33": "Ocorreu um erro ao ler o arquivo de configuração.",
        "str:34": "Provavelmente o repositório não foi criado. Use: dotctrl init [--auto | --git ]",
        "str:35": "Limpeza concluida!",
        "str:36": "Nada a limpar!",
        "str:37": f"""

        Arquivos com o mesmo nome foram encontrados no repositório {__info__['name']} e no local de origem.
        Para substituir os do repositorio do {__info__['name']}, use a opção --force (--f).
        """,
    },
}
