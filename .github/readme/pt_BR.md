<h1 align="center">
  <a href="https://github.com/snakypy/dotctrl">
    <img alt="Dotctrl" src="https://raw.githubusercontent.com/snakypy/assets/main/dotctrl/images/dotctrl-transparent.png" width="auto">
  </a>
</h1>

<h1 align="center"> A ferramenta de controle de "dotfiles". </h1>

[![Tests](https://github.com/snakypy/dotctrl/workflows/Tests/badge.svg)](https://github.com/snakypy/dotctrl/actions)
[![Python Versions](https://img.shields.io/pypi/pyversions/dotctrl)](https://pyup.io/repos/github/snakypy/dotctrl/)
[![Updates](https://pyup.io/repos/github/snakypy/dotctrl/shield.svg)](https://pyup.io/repos/github/snakypy/dotctrl/)
[![Python Whell](https://img.shields.io/pypi/wheel/dotctrl)](https://pypi.org/project/wheel/)
[![PyPI](https://img.shields.io/pypi/v/dotctrl)](https://pypi.org/project/dotctrl/#history)
[![PyPI - Implementation](https://img.shields.io/pypi/implementation/dotctrl)](https://pypi.org/project/dotctrl)
[![Isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![Code style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/dotctrl)](https://pypi.org/project/dotctrl/#files)
[![GitHub license](https://img.shields.io/github/license/snakypy/dotctrl)](https://github.com/snakypy/dotctrl/blob/main/LICENSE)

----------------

<div align="center">
  <sub>Construído com ❤︎ por:
  <a href="https://williamcanin.github.io" target="_blank">William Canin</a> no tempo livre,
   ao som da playlist: <a href="https://open.spotify.com/playlist/48brJJZdVifY79QAFmEImq?si=GmsvfKqATpG4p72ZeVClIQ" target="_blank">Bursting Of The Tympanum</a></sub>
</div>
<br>
<br>

<div class="sumary">
  <h1> Sumário </h1>
  <ul>
      <li>
          <a href="#sobre">Sobre</a>
      </li>
      <li>
          <a href="#características">Características</a>
      </li>
      <li>
          <a href="#requisitos">Requisitos</a>
      </li>
      <li>
          <a href="#instalando">Instalando</a>
      </li>
      <li>
          <a href="#usando">Usando</a>
          <ul>
              <li>
                  <a href="#init">init</a>
              </li>
              <li>
                  <a href="#pull">pull</a>
              </li>
              <li>
                  <a href="#link">link</a>
              </li>
              <li>
                  <a href="#unlink">unlink</a>
              </li>
              <li>
                  <a href="#restore">restore</a>
              </li>
              <li>
                  <a href="#repo">repo</a>
              </li>
              <li>
                  <a href="#find">find</a>
              </li>
              <li>
                  <a href="#config">config</a>
              </li>
          </ul>
      </li>
      <li>
          <a href="#flags-globais">Flags Globais</a>
      </li>
      <li>
          <a href="#arquivo-de-configuração-dotctrljson">Arquivo de configuração (dotctrl.json)</a>
      </li>
      <li>
          <a href="#variável-de-ambiente">Variável de ambiente</a>
      </li>
      <li>
          <a href="#atualizando">Atualizando</a>
      </li>
      <li>
          <a href="#mais-comandos">Mais Comandos</a>
      </li>
      <li>
          <a href="#extras">Extras</a>
          <ul>
              <li>
                  <a href="#deploy-e-clone-do-repositório-dotctrl">Deploy e Clone do repositório Dotctrl</a>
              </li>
          </ul>
      </li>
      <li>
          <a href="#doação">Doação</a>
      </li>
      <li>
          <a href="#licença">Licença</a>
      </li>
  </ul>
</div>

# Sobre

Inicialmente, o **Dotctrl** surgiu apenas para controlar "aquivos dotfiles", porem, ao decorrer, ele se tornou mais do que isso.
Agora, o **Dotctrl** é um mantenedor de qualquer tipo arquivo e pasta dentro do seu próprio repositório particular.

Isso é demais!

O **Dotctrl** irá gerenciar os elementos do diretório HOME do usuário; funcionando em cima de um arquivo de configuração (`dotctrl.json`) que contém os caminhos do local de origem dos elementos.

O **Dotctrl** é compatível com [Linux](https://www.kernel.org/) ou [macOS](https://www.apple.com/macos/).


Veja uma demonstração:

![](https://raw.githubusercontent.com/snakypy/assets/main/dotctrl/gifs/demo.gif)

# Características

* Suporta aos idiomas: Inglês Americano e Português brasileiro;
* Crie (ou não) vários repositórios para seus elementos;
* Abandone a criação de links simbólicos manuais enormes;
* O repositório armazena a mesma estrutura de caminho que seu local (`$HOME`) original;
* Gerencie elementos únicos ou em massa;
* Restaure os elementos do repositório para sua localização original com um único comando;
* E muito mais :)

# Requisitos

Para funcionar corretamente, você precisará primeiro:

- [`Python`](https://python.org) (v3.9 ou recente);
- [`Pip`](https://pip.pypa.io/en/stable/) (v19.3 ou recente) deve ser instalado;
- [`Git`](https://git-scm.com/downloads) (v2.0 ou recente);
- Um desse editor [vim](https://www.vim.org/), [nano](https://www.nano-editor.org/), [emacs](https://www.gnu.org/software/emacs/) ou [micro](https://micro-editor.github.io/) devem ser instalado;


# Instalando

É hora de instalar o **Dotctrl**. Para fazer isso, faça:

```shell
python3 -m pip install dotctrl --user
```

> NOTA: Se você estiver instalando no ambiente local do usuário, certifique-se de adicionar as variáveis de ambiente ao arquivo `zshrc`
> ou arquivo `.bashrc`.

# Usando

## init

Após instalar o pacote, você precisa criar o repositório **Dotctrl** em uma pasta vazia no local do sua
escolha. Recomendamos sempre criar no diretório raiz **/home** ou **/Users**, pois criando na pasta do usuário, pode ser
perdido se o usuário for excluído. Com isso, veja o exemplo abaixo:

Linux:

```shell
sudo mkdir -p /home/.dotfiles; cd $_
sudo chown -R $(whoami) /home/.dotfiles
sudo chmod -R 700 /home/.dotfiles
dotctrl init
```

macOS:

```shell
sudo mkdir -p /Users/.dotfiles; cd $_
sudo chown -R $(id -un) /Users/.dotfiles
sudo chmod -R 700 /Users/.dotfiles
dotctrl init
```

### --auto

Você pode contornar todos esses comandos acima usando a flag `--auto`. O **Dotctrl** criará automaticamente uma base
diretório para armazenar os dados, no entanto, você **DEVE** ter permissão sudo.

> Recomendamos usar fortemente está opção caso tenha permissão.

```shell
dotctrl init --auto
```

### --git

Esta flag faz com que o **Dotctrl** crie um repositório [git](https://git-scm.com) dentro do repositório **Dotctrl**.

```shell
dotctrl init --git
```

Você também pode combinar está flag com a flag [`--auto`](#--auto):

```shell
dotctrl init --auto --git
```

## pull

Com a base já criada, é hora de você PUXAR os elementos para a base do **Dotctrl** com o comando `pull`.

Puxe **UM** [elemento]() para o repositório **Dotctrl**:

```shell
dotctrl pull --e .zprofile
```

Se você quiser fazer um **pull** massivo, faça:

```shell
dotctrl pull
```

> Nota: Esta opção só é possível se você passar os [elements](#section-elements) manualmente no arquivo **dotctrl.json** ou não ter limpadado o [registro](#autoclean).


## link

Depois de puxar o(s) elemento(s), crie links simbólicos para eles em seus locais originais:

```shell
dotctrl link --e .zprofile
```

Se você quiser realizar um **link** massivo, faça:

```shell
dotctrl link
```

> Nota: Esta opção só é possível se você passar os [elements](#section-elements) manualmente no arquivo **dotctrl.json** ou não ter limpado o [registro](#autoclean).

## unlink

Desvincule o elemento do repositório com o local de origem:

```shell
dotctrl unlink --e .zprofile
```

Se você quiser **desvincular** elementos de forma massiva, faça:

```shell
dotctrl unlink
```

> Nota: Esta opção só é possível se você passar os [elements](#section-elements) manualmente no arquivo **dotctrl.json** ou não ter limpadado o [registro](#autoclean).

## restore

Este comando irá tirar um elemento do repositório **Dotctrl** e restaurar para seu local original:

```shell
dotctrl restore --e .zprofile
```

Se você quiser realizar uma **restauração** massiva, faça:

```shell
dotctrl restore
```

> Nota: Por padrão, ao restaurar elemento(s) para o local de origem, o **Dotctrl** NÃO remove os elemento do registro
> (`dotctrl.json`). Para limpar, veja [--autoclean](#autoclean).

## repo

Este comando trás informações do repositório, veja abaixo alguns de seu subcomandos:

### --check

Faça uma verificação para ver se há elementos a serem vinculados:

```shell
dotctrl repo --check
```

### --ls

Verifique os elementos já importados no repositório do **Dotctrl**.

```shell
dotctrl repo --ls
```

### --info

Com o comando abaixo você pode ver algumas informações do repositório **Dotctrl**, como quantidade de pastas e arquivos,
o caminho absoluto do repositório e se a variável de ambiente `DOTCTRL_PATH` estiver ativa.

```shell
dotctrl repo --info
```

## find

Pesquisa qualquer elemento dentro do repositório do **Dotctrl**. Para isso, use o comando:

```shell
dotctrl find --name .zprofile
```

> Nota: Envolva o elemento a ser encontrar com aspas duplas caso o mesmo tenha espaços no nome.

## config

Este comando irá manipular o arquivo de configuração do **Dotctrl**, veja abaixo alguns subcomandos do mesmo.

### --autoclean

Faz uma limpeza nos elementos presentes no arquivo de configuração do **Dotctrl**.
Qualquer elemento que estiver presente no arquivo de configuração do **Dotctrl** e não EXISTIR no repositório, serão eliminados do arquivo de configuração.

Geralmente o `--autoclean` é usado após usar o comando de [restauração](#restore) de elementos.

```shell
dotctrl config --autoclean
```

### --view

Dê uma espiada no arquivo de configuração do **Dotctrl** pelo terminal.

### --open

Permite editar o arquivo de configuração do **Dotctrl** no próprio terminal usando o comando:

```shel
dotctrl config --open
```

> Nota: Usa por padrão o editor `vim`, caso não tenha, irá tentar usar o `nano`, `emacs` ou `micro`.

### --lang

Use está flag para alterar o idioma do **Dotctrl**. No momento, o **Dotctrl** dá suporte para 2 (dois) idiomas, eles são: **Inglês Americano** e **Português Brasileiro**. Ao usar o comando abaixo, irá mostrar uma lista para você escolher qual idioma quer usar. A alteração é instantânea.

```shel
dotctrl config --lang
```

## Flags globais

### --e (--element)

A flag **--e** ou **--element**, é responsável por manipular um elemento especifico do repositório **Dotctrl**.

Esta flag deve receber um elemento sem o caminho absoluto, apenas o relativo a partir da `$HOME`.

Exemplos:

* `dotctrl pull --e .zprofile`
* `dotctrl link --e .zprofile`
* `dotctrl unlink --e .zprofile`
* `dotctrl restore --e .zprofile`

Se o elemento tiver espaços no nome, envolva-o entre aspas duplas. Exemplo: `dotctrl pull --e "arquivo legal.txt"`

### --f (--force)

A flag **--f** ou **--force**, força literalmente o uso do comando, impedindo que algo impeça sua conclusão. Esta opção está presente em todos os comandos que manipula os elementos, esses comandos são o: `pull`, `link`, `unlink` e `restore`.


## Arquivo de configuração (dotctrl.json)

Este é um exemplo de uma estrutura completa do arquivo de configuração (`dotctrl.json`) do **Dotctrl**:

```json
{
    "dotctrl": {
        "config": {
            "editor": "vim",
            "language": "pt_BR"
        },
        "elements": [
            ".zshrc",
            ".config/xfce4/terminal/terminalrc",
            ".config/Code/User",
            "Images/Wedding"
        ],
    }
}
```

## Variável de ambiente

Por padrão, **Dotctrl** funciona com vários diretórios, o que faz com que você precise usá-lo em um determinado diretório que você criou para seus elementos.

Se você quiser usar **Dotctrl** em qualquer PATH, você precisa criar uma variável de ambiente que **Dotctrl** disponibiliza. Esta variável de ambiente é `DOTCTRL_PATH`.

Você deve inserir a variável `DOTCTRL_PATH` em seu sistema operacional contendo o diretório onde estarão seus dotfiles. Por exemplo, em seu arquivo `.bashrc` ou `.zshrc`:

Linux:

```shell
export DOTCTRL_PATH="/home/.dotfiles"
```
ou

macOS:

```shell
export DOTCTRL_PATH="/Users/.dotfiles"
```

> NOTA: Lembre-se, ao criar esta variável de ambiente, você não poderá criar outros repositórios para **Dotctrl**.


## Atualizando

Se **Dotctrl** tiver novos recursos, atualize a linha de comando abaixo:

```shell
python3 -m pip install dotctrl -U --user
```

## Mais comandos

Para obter mais informações de comando, use:

```
dotctrl [--help | -h]
```

## Extras

### Deploy e Clone do repositório Dotctrl

Agora que você tem o controle de seus elementos, é hora de fazer o deploy dos mesmo em um serviço de git.
Este exemplo abaixo mostrará como realizar o deploy e clone no [GitHub](https://github.com).

1 - Deploy:

A - Entrando na pasta raiz criada do **Dotctrl**:

Linux:

```shell
cd /home/.dotfiles
```

macOS:

```shell
cd /Users/.dotfiles
```

B - Criando repositório git, commit e salvando (push)

```shell
git remote add origin git@github.com:<YOUR USER>/dotfiles.git
git init
git add .
git commit -m "Update"
git push origin main
```

2 - Clone:

Você também pode clonar qualquer diretório de sua escolha, mas vamos manter o diretório de compilação de exemplo acima. Siga os passos:

Linux:

```shell
sudo mkdir -p /home/.dotfiles
sudo chmod -R 770 /home/.dotfiles
cd /home/.dotfiles
git clone git@github.com:<YOUR USER>/dotfiles.git .
dotctrl link --f
```

macOS:

```shell
sudo mkdir -p /Users/.dotfiles
sudo chmod -R 770 /Users/.dotfiles
cd /Users/.dotfiles
git clone git@github.com:<YOUR USER>/dotfiles.git .
dotctrl link --f
```

## Doação

Clique na imagem abaixo para ser redirecionado aos formulários de doação:

<div class="donate">
  <a href="https://github.com/snakypy/donations/blob/main/README.md">
    <img width="160" height="100" src="https://raw.githubusercontent.com/snakypy/donations/main/svg/donate/donate-hand.svg" alt="Donations"/>
  </a>
</div>

É muito importante você fazer uma doação para motivar a continuação de desenvolvimento do **Dotctrl**. :)

## Licença

O projeto está disponível como código aberto sob os termos da [Licença MIT](https://github.com/snakypy/dotctrl/blob/main/LICENSE) ©

## Creditos

Veja, [AUTHORS](https://github.com/snakypy/dotctrl/blob/main/AUTHORS.rst).
