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
[![MaxLength](https://img.shields.io/badge/MaxLength-79-green.svg)](https://shields.io/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/dotctrl)](https://pypi.org/project/dotctrl/#files)
[![GitHub license](https://img.shields.io/github/license/snakypy/dotctrl)](https://github.com/snakypy/dotctrl/blob/main/LICENSE)
[![PEP8](https://img.shields.io/badge/code%20style-pep8-orange.svg)](https://www.python.org/dev/peps/pep-0008/)
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

Initially, **Dotctrl** was created just to control "dotfiles files", however,
in the course, it became more than that.
**Dotctrl** is now a maintainer of any file and folder type within its own
private repository.

This is too much!

**Dotctrl** will manage the elements of the user's HOME directory; running on
top of a configuration file (`dotctrl.json`) that contains the paths to the
origin location of the elements.

All elements managed by **Dotctrl** are kept in the repository/folder
"**dotctrl**".

See a demo:

![](https://raw.githubusercontent.com/snakypy/assets/main/dotctrl/gifs/demo.gif)

# Features

* language support: American English and Brazilian Portuguese;
* create (or not) multiple repositories for your elements;
* abandon the creation of huge manual symlinks;
* will store the same path structure as your original location (`$HOME`);
* manage single or bulk elements;
* restore repository elements to their original location with a single command;
* and much more :)

# Requirements

To work properly, you will first need:

- [`Linux`](https://www.kernel.org) or [`macOS`](https://www.apple.com/macos)
- [`Python`](https://python.org) (v3.9 or recent);
- [`Pip`](https://pip.pypa.io/en/stable/) (v19.3 or recent) must be installed;
- [`Git`](https://git-scm.com/downloads) (v2.0 or recent);
- One of this editor [vim](https://www.vim.org/), [nano](https://www.nano-editor.org/), [emacs](https://www.gnu.org/software/emacs/) or [micro](https://micro-editor.github.io/) must be installed;


# Installing

It's time to install **Dotctrl**. To do this, do:

```shell
python3 -m pip install dotctrl --user
```

> NOTE: If you are installing in the user's local environment, be sure to add
> the environment variables to the `zshrc` file
> or `.bashrc` file.

# Using

## init

After installing the package, you need to create the **Dotctrl** repository in
an empty folder in your
choice. We always recommend creating **/home** or **/Users** in the root
directory, because creating in the user's folder can be
lost if user is deleted. With that, see the example below:

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

You can bypass all of these commands above using the `--auto` flag. **Dotctrl**
will automatically create a base
directory to store the data, however you **MUST** have sudo permission.

> We strongly recommend using this option if you have permission.

```shell
dotctrl init --auto
```
### --git

This flag causes **Dotctrl** to create a [git](https://git-scm.com) repository
within the **Dotctrl** repository.

```shell
dotctrl init --git
```

You can also combine this flag with the [`--auto`](#--auto) flag:

```shell
dotctrl init --auto --git
```
## pull

With the base already created, it's time for you to PULL the elements to the
base of **Dotctrl** with the `pull` command.

Pull **single** [element]() to the **Dotctrl** repository:

```shell
dotctrl pull --e .zprofile
```

If you want to do a massive **pull**, do:

```shell
dotctrl pull
```

> Note: This option is only possible if you pass the
> [elements](#section-elements) manually in the **dotctrl.json** file or have
> not cleaned the [registry](#autoclean).

## link

After pulling the element(s), create symlinks to them in their original
locations:

```shell
dotctrl link --e .zprofile
```

If you want to perform a massive **link**, do:

```shell
dotctrl link
```

> Note: This option is only possible if you pass the
> [elements](#section-elements) manually in the **dotctrl.json** file or have
> not cleaned the [record](#autoclean).

## unlink

Unlink the repository element with the source location:

```shell
dotctrl unlink --e .zprofile
```

If you want to **unlink** elements massively, do:

```shell
dotctrl unlink
```

> Note: This option is only possible if you pass the
> [elements](#section-elements) manually in the **dotctrl.json** file or
> have not cleaned the [record](#autoclean).

## restore

This command will take an element from the **Dotctrl** repository and restore
it to its original location:

```shell
dotctrl restore --e .zprofile
```

If you want to perform a massive **restore**, do:

```shell
dotctrl restore
```

> Note: By default, when restoring element(s) to their original location,
> **Dotctrl** does NOT remove the elements from the registry
> (`dotctrl.json`). To clean, see [--autoclean](#autoclean).

## repo

This command brings information from the repository, see below some of its
subcommands:

### --check

Check to see if there are elements to link:

```shell
dotctrl repo --check
```

### --ls

Check the elements already imported into the **Dotctrl** repository.

```shell
dotctrl repo --ls
```

### --info

With the command below you can see some information from the **Dotctrl**
repository, such as the number of folders and files,
the absolute path of the repository and if the environment variable
`DOTCTRL_PATH` is active.

```shell
dotctrl repo --info
```

## find

Searches for any element within the **Dotctrl** repository. To do this, use
the command:

```shell
dotctrl find --name .zprofile
```

> Note: Enclose the element to be found with double quotes if it has spaces
> in the name.

## config

This command will manipulate the **Dotctrl** configuration file, see below
some of its subcommands.

### --autoclean

Clean up the elements present in the **Dotctrl** configuration file.
Any element that is present in the **Dotctrl** configuration file and does not
EXIST in the repository will be eliminated from the configuration file.

Usually `--autoclean` is used after using the command to [restore](#restore)
elements.

```shell
dotctrl config --autoclean
```

### --view

Take a peek at the **Dotctrl** configuration file from the terminal.

### --open

Allows you to edit the **Dotctrl** configuration file in the terminal itself
using the command:

```shel
dotctrl config --open
```

> Note: It defaults to the `vim` editor, if not, it will try to use `nano`,
> `emacs` or `micro`.

### --lang

Use this flag to change the language of **Dotctrl**. **Dotctrl** currently
supports 2 (two) languages, they are: **American English** and
**Brazilian Portuguese**. When using the command below, it will show a list
for you to choose which language you want to use. The change is instantaneous.

```shel
dotctrl config --lang
```

## Global flags

### --e (--element)

The **--e** or **--element** flag is responsible for handling a specific
element of the **Dotctrl** repository.

This flag must receive an element without the absolute path, only the relative
one from `$HOME`.

Examples:

* `dotctrl pull --e .zprofile`
* `dotctrl link --e .zprofile`
* `dotctrl unlink --e .zprofile`
* `dotctrl restore --e .zprofile`

If the element has spaces in the name, enclose it in double quotes. Example:
`dotctrl pull --e "file legal.txt file"`

### --f (--force)

The **--f** or **--force** flag literally forces the use of the command,
preventing something from preventing its completion. This option is present in
all commands that manipulate elements, these commands are: `pull`, `link`,
`unlink` and `restore`.


## Configuration file (dotctrl.json)

This is an example of a complete **Dotctrl** configuration file
(`dotctrl.json`) structure:

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
        ]
    }
}
```

## Environment Variable

By default, **Dotctrl** works with multiple directories, which makes you need
to use it in a certain directory you created for your elements.

If you want to use **Dotctrl** in any PATH, you need to create an environment
variable that **Dotctrl** makes available. This environment variable is
`DOTCTRL_PATH`.

You must enter the `DOTCTRL_PATH` variable in your operating system containing
the directory where your dotfiles will be. For example, in your `.bashrc` or
`.zshrc` file:

Linux:

```shell
export DOTCTRL_PATH="/home/.dotfiles"
```
or

macOS:

```shell
export DOTCTRL_PATH="/Users/.dotfiles"
```

> NOTE: Remember, when creating this environment variable, you will not be
> able to create other repositories for **Dotctrl**.


## Updating

If **Dotctrl** has new features, please update the command line below:

```shell
python3 -m pip install dotctrl -U --user
```

## More commands

For more command information, use:

```
dotctrl [--help | -h]
```

## Extras

### Deploy and Clone from Dotctrl repository

Now that you have control of your elements, it's time to deploy them to a git
service.
This example below will show you how to deploy and clone on
[GitHub](https://github.com).

1 - Deploy:

A - Entering the root folder created by **Dotctrl**:

Linux:

```shell
cd /home/.dotfiles
```

macOS:

```shell
cd /Users/.dotfiles
```

B - Creating git repository, commit and saving (push)

```shell
git remote add origin git@github.com:<YOUR USER>/dotfiles.git
git init
git add .
git commit -m "Update"
git push origin main
```

2 - Clone:

You can also clone any directory of your choice, but we'll keep the example
build directory above. Follow the steps:

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

## Donation

Click on the image below to be redirected to the donation forms:

<div class="donate">
  <a href="https://github.com/snakypy/donations/blob/main/README.md">
    <img width="160" height="100" src="https://raw.githubusercontent.com/snakypy/donations/main/svg/donate/donate-hand.svg" alt="Donations"/>
  </a>
</div>

It is very important that you make a donation to motivate further development
of **Dotctrl**. :)

## License

The project is available as open source under the terms of the
[MIT License](https://github.com/snakypy/dotctrl/blob/main/LICENSE) ©

## Credits

See, [AUTHORS](https://github.com/snakypy/dotctrl/blob/main/AUTHORS.rst).
