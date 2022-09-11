Languages: [Português Brasileiro](https://github.com/snakypy/dotctrl/blob/main/.github/readme/pt_BR.md)

<h1 align="center">
  <a href="https://github.com/snakypy/dotctrl">
    <img alt="Dotctrl" src="https://raw.githubusercontent.com/snakypy/assets/main/dotctrl/images/dotctrl-transparent.png" width="auto">
  </a>
</h1>

<h1 align="center">The "dotfiles" control tool.</h1>

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
  <sub>Built with ❤︎ by:
  <a href="https://williamcanin.github.io" target="_blank">William Canin</a> in free time,
    to the sound of the playlist: <a href="https://open.spotify.com/playlist/48brJJZdVifY79QAFmEImq?si=GmsvfKqATpG4p72ZeVClIQ" target="_blank">Bursting Of The Tympanum</a></sub>
</div>
<br>
<br>

<div class="sumary">
  <h1> Sumary </h1>
  <ul>
      <li>
          <a href="#about">About</a>
      </li>
      <li>
          <a href="#features">Features</a>
      </li>
      <li>
          <a href="#requirements">Requirements</a>
      </li>
      <li>
          <a href="#installing">Installing</a>
      </li>
      <li>
          <a href="#using">Using</a>
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
          <a href="#global-flags">Global flags</a>
      </li>
      <li>
          <a href="#configuration-file-dotctrljson">Configuration file (dotctrl.json)</a>
      </li>
      <li>
          <a href="#environment-variable">Environment Variable</a>
      </li>
      <li>
          <a href="#updating">Updating</a>
      </li>
      <li>
          <a href="#more-commands">More Commands</a>
      </li>
      <li>
          <a href="#extras">Extras</a>
          <ul>
              <li>
                  <a href="#deploy-and-clone-from-dotctrl-repository">Deploy and Clone from Dotctrl repository</a>
              </li>
          </ul>
      </li>
      <li>
          <a href="#donation">Donation</a>
      </li>
      <li>
          <a href="#license">License</a>
      </li>
  </ul>
</div>

# About

Initially, **Dotctrl** was created just to control "dotfiles files", however, in the course, it became more than that.
**Dotctrl** is now a maintainer of any file and folder type within its own private repository.

This is too much!

**Dotctrl** will manage the elements of the user's HOME directory; running on top of a configuration file (`dotctrl.json`) that contains the paths to the origin location of the elements.

**Dotctrl** is compatible with [Linux](https://www.kernel.org/) or [macOS](https://www.apple.com/macos/).


See a demo:

![](https://raw.githubusercontent.com/snakypy/assets/main/dotctrl/gifs/demo.gif)

# Features

* Language support: American English and Brazilian Portuguese;
* Create (or not) multiple repositories for your elements;
* Abandon the creation of huge manual symlinks;
* O armazenará a mesma estrutura de caminho que seu local (`$HOME`) original;
* Manage single or bulk elements;
* Restore repository elements to their original location with a single command;
* And much more :)

# Requirements

To work properly, you will first need:

- [`Python`](https://python.org) (v3.9 ou recente);
- [`Pip`](https://pip.pypa.io/en/stable/) (v19.3 ou recente) deve ser instalado;
- [`Git`](https://git-scm.com/downloads) (v2.0 ou recente);
- Um desse editor [vim](https://www.vim.org/), [nano](https://www.nano-editor.org/), [emacs](https://www.gnu.org/software/emacs/) ou [micro](https://micro-editor.github.io/) devem ser instalado;


# Installing

It's time to install **Dotctrl**. To do this, do:

```shell
python3 -m pip install dotctrl --user
```

> NOTE: If you are installing in the user's local environment, be sure to add the environment variables to the `zshrc` file
> or `.bashrc` file.

# Using

## init

After installing the package, you need to create the **Dotctrl** repository in an empty folder in your
choice. We always recommend creating **/home** or **/Users** in the root directory, because creating in the user's folder can be
lost if user is deleted. With that, see the example below:

Linux:

```shell
sudo mkdir -p /home/.dotfiles/linux; cd $_
sudo chown -R <YOU USER> /home/.dotfiles
sudo chmod -R 700 /home/.dotfiles
dotctrl init
```

macOS:

```shell
sudo mkdir -p /Users/.dotfiles/linux; cd $_
sudo chown -R <YOU USER> /Users/.dotfiles
sudo chmod -R 700 /Users/.dotfiles
dotctrl init
```

### --auto

You can bypass all of these commands above using the `--auto` flag. **Dotctrl** will automatically create a base
directory to store the data, however you **MUST** have sudo permission.

> We strongly recommend using this option if you have permission.

```shell
dotctrl init --auto
```
### --git

This flag causes **Dotctrl** to create a [git](https://git-scm.com) repository within the **Dotctrl** repository.

```shell
dotctrl init --git
```

You can also combine this flag with the [`--auto`](#--auto) flag:

```shell
dotctrl init --auto --git
```
## pull

With the base already created, it's time for you to PULL the elements to the base of **Dotctrl** with the `pull` command.

Pull **single** [element]() to the **Dotctrl** repository:

```shell
dotctrl pull --e .zprofile
```

If you want to do a massive **pull**, do:

```shell
dotctrl pull
```

> Note: This option is only possible if you pass the [elements](#section-elements) manually in the **dotctrl.json** file or have not cleaned the [registry](#autoclean).

## link

After pulling the element(s), create symlinks to them in their original locations:

```shell
dotctrl link --e .zprofile
```

If you want to perform a massive **link**, do:

```shell
dotctrl link
```

> Nota: Esta opção só é possível se você passar os [elements](#section-elements) manualmente no arquivo **dotctrl.json** ou não ter limpadado o [registro](#autoclean).

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

## Global flags

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
export DOTCTRL_PATH="/home/.dotfiles/linux"
```
ou

macOS:

```shell
export DOTCTRL_PATH="/Users/.dotfiles/macos"
```

> NOTA: Lembre-se, ao criar esta variável de ambiente, você não poderá criar outros repositórios para **Dotctrl**.


## Updating

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
git clone git@github.com:<YOUR USER>/dotfiles.git
cd /home/.dotfiles/linux
dotctrl link --f
```

macOS:

```shell
sudo mkdir -p /Users/.dotfiles
sudo chmod -R 770 /Users/.dotfiles
cd /Users/.dotfiles
git clone git@github.com:<YOUR USER>/dotfiles.git
cd /home/.dotfiles/macos
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
