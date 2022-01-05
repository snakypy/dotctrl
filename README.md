<h1 align="center">
  <a href="https://github.com/snakypy/dotctrl">
    <img alt="Dotctrl" src="https://raw.githubusercontent.com/snakypy/assets/main/dotctrl/images/dotctrl-transparent.png" width="auto">
  </a>
</h1>

<h1 align="center"> The dotfile management tool. </h1>

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
[![GitHub license](https://img.shields.io/github/license/snakypy/dotctrl)](https://github.com/snakypy/dotctrl/blob/master/LICENSE)

----------------

<div align="center">
  <h4>
    <a href="#features">Features</a> |
    <a href="#requirements">Requirements</a> |
    <a href="#installing">Installing</a> |
    <a href="#using">Using</a> |
    <a href="#configuration">Configuration</a> |
    <a href="#environment-variable">Environment variable</a> |
    <a href="#upgrading">Upgrade</a> |
    <a href="#donation">Donation</a> |
  </h4>
  <h5>
    | <a href="#more-commands">More Commands</a> |
  </h5>
</div>

<div align="center">
  <sub>Built with ❤︎ by:
  <a href="https://williamcanin.github.io" target="_blank">William Canin</a> in free time,
  to the sound of the playlist: <a href="https://open.spotify.com/playlist/48brJJZdVifY79QAFmEImq?si=GmsvfKqATpG4p72ZeVClIQ" target="_blank">Bursting Of The Tympanum</a></sub>
</div>
<br>
<br>

**Dotctrl** is a package for managing your "dotfiles" on Linux or macOS. **Dotctrl** works on top of a configuration file that contains the absolute paths of the place of origin of dotfiles.

## Features

* Create multiple repositories for your files;
* Stay free to create manual links;
* Automatically manages dotfiles ending with rc in the user's `$HOME`;
* Automatically manages the main configuration files of the editors: Atom, Sublime Text, Visual Studio Code;
* The **Dotctrl** repository stores the same path structure as its original location;
* Manage single or bulk elements;
* Restores the elements of the repository to their original location with a single command;
* And much more :)

## Requirements

To work correctly, you will first need:

- [`Python`](https://python.org) (v3.7 or recent);
- [`Pip`](https://pip.pypa.io/en/stable/) (v19.3 or recent) must be installed;
- [`Git`](https://git-scm.com/downloads) (v2.0 or recent);
- One of that editor [vim](https://www.vim.org/), [nano](https://www.nano-editor.org/) or [emacs](https://www.gnu.org/software/emacs/) must be installed;


## Installing

It's time to install **Dotctrl**. To do this, do:

```shell
$ python3 -m pip install dotctrl --user
```

> NOTE: If you are installing to the user's local environment, be sure to add the environment variables to the `zshrc` or `.bashrc` file.

## Using

**Init**

After installing the package, you need to create the Dotctrl repository in an empty folder in the location of your choice. We recommend always creating in the users' root directory, because creating in the user's folder you can get lost if the user is deleted. With that, the example below:

Linux:

```shell
$ sudo mkdir -p /home/.dotfiles/linux
$ sudo chown <YOU USER> /home/.dotfiles
$ sudo chmod 700 -R /home/.dotfiles
$ mkdir /home/.dotfiles/linux; cd $_
$ dotctrl init
```

macOS:

```shell
$ sudo mkdir -p /Users/.dotfiles/macos
$ sudo chown <YOU USER> /Users/.dotfiles
$ sudo chmod 700 /Users/.dotfiles
$ mkdir /Users/.dotfiles/macos; cd $_
$ dotctrl init
```

> TIP: You can create several subfolders with different Dotctrl repository.

**Pull**

Pull an element into the **Dotctrl** repository:

```shell
$ dotctrl pull --element=".zprofile"
```

> Note: You must enter the element path without the `HOME` path.

If you want to perform a massive **pull**, do:

```shell
$ dotctrl pull
```

> Note: This option is only possible if you pass the [elements](#section-elements) in the **dotctrl.json** file.

**Link**

After pulling the element(s), create symbolic links to them in their original locations:

```shell
$ dotctrl link --element=".zprofile"
```

> Note: You must enter the element path without the `HOME` path.

If you want to perform a massive **link**, do:

```shell
$ dotctrl link
```

> Note: If there is a link already created, **Dotctrl** will inform you to use the `--force` option.

**Check**

Make a check to see if there are elements to be linked:

```shell
$ dotctrl check
```

**List**

List the elements of the repository:

```shell
$ dotctrl list
```

**Unlink**

Unlink element from the repository with the source location:

```shell
$ dotctrl unlink --element=".zprofile"
```

> NOTE: You must enter the element path without the `HOME` path.

If you want to perform a massive **unlink**, do:

```shell
$ dotctrl unlink
```

**Restore**

Restore an element from the repository to its original location:

```shell
$ dotctrl restore --element=".zprofile"
```

> NOTE: You must enter the element path without the `HOME` path.

If you want to perform a massive **restore**, do:

```shell
$ dotctrl restore
```
> Note: > Note: If there is already an element created in the original location, **Dotctrl** will inform you to use the `--force` option.

**Remove** `(DANGER)`

The **remove** option is irreversible. Removes element (s) from the repository and its symbolic links in the place of origin if it exists.

This option of **remove**, is interactive, that is, you will have questions precisely because it is an irreversible option.

To remove an element from the repository and its symbolic link, do:

```shell
$ dotctrl remove
```
This will open a list of elements from the repository for the remove user. The user can only choose one element at a time.

If you want to remove elements in bulk, use the `--all` option

```/shell
$ dotctrl remove --all
```

To perform the removal without interactive mode, use the `--noconfirm` option. DANGER!



**For more command, run: `dotctrl -h`**

## Configuration

**Dotctrl** works on top of a configuration file created in the Dotctrl repository, which is the **dotctrl.json** file.

You can open the **Dotctrl** configuration file in the terminal itself using the command:

```shel
$ dotctrl config --open
```

### Understanding each section `dotctrl.json`:

#### Section `config`:

* In the **editor** key, you can choose an editor of your choice. You must enter the publisher's binary, for example: **vim**, **nano**, etc. If you leave it blank, **Dotctrl** will select one of these terminal text editors: **vim**, **nano**, **emacs**, and **micro**.

```json
{

        "config": {
            "editor": ""
        }

}
```

#### Section `elements`:

* **elements**: As the name says, "*elements*" will store the absolute path of the elements you want to place inside the **Dotctrl** repository in a **list**. Examples:

```json
{

        "elements": [".foo/foo.conf",
                     ".bar/bar.conf",
                     ".foo.conf"]

}
```

The `elements` option also accepts complete folders instead of just files:

```json
{

        "elements": [".foo",
                     ".bar"]

}
```

For madness but true, **Dotctrl** also manages files and folders without points:

```json
{

        "elements": ["Documents/foo.txt",
                     "Images/bar.jpg"]

}
```

You must place files (<u>or folders</u>) that are inside the user's **$HOME**, as this is how **Dotctrl** works, only with elements in the user's $HOME.



#### Section `smart`:

This section is very cool. It is the smart section of **Dotctrl**, where you will find configuration files and dotfiles for certain applications. :)

```json
{

        "smart": {
            "rc": {
                "enable": true
            },
            "text_editors": {
                "enable": true
            }
        }

}
```

* **rc.enable:** Option: `true`|`false`. If this option is `true`, **Dotctrl** will search for all dotfiles in the user's *$HOME* directory containing *rc* at the end. **Default:** `false`
* **text_editors.enable:** Option: `true`|`false`. If this option is `true`, **Dotctrl** will search for the main dotfiles of the following text editors: [Atom](https://atom.io), [Sublime Text](https://www.sublimetext.com/), and [Visual Studio Code](https://code.visualstudio.com/). **Default:** `false`

**Example configuration file:**

```json
{
    "dotctrl": {
        "config": {
            "editor": "vim"
        },
        "elements": [
            ".zprofile",
            ".gitconfig",
            ".config/xfce4/terminal/terminalrc"
        ],
        "smart": {
            "rc": {
                "enable": true
            },
            "text_editors": {
                "enable": false
            }
        }
    }
}
```

## Environment variable

By default, **Dotctrl** works with multiple directories, which makes you have to use it in a certain directory you created for your dotfiles. If you want to use **Dotctrl** in any PATH, you need to create an environment variable that **Dotctrl** makes available. This environment variable is `DOTCTRL_PATH`. You must create it on your operating system containing the directory where your dotfiles will be. For example, in your `.bashrc` or `.zshrc` file:


Linux:

```shell
export DOTCTRL_PATH="/home/.dotfiles/linux"
```

macOS:

```shell
export DOTCTRL_PATH="/Users/.dotfiles/macos"
```

> Remember, by creating this environment variable, you will not be able to create other directories for **Dotctrl**.


## Upgrading

If **Dotctrl** has any new features, please update the command line below:

```shell
$ python3 -m pip install dotctrl -U --user
```

## More Commands

For more command information, use:

```
$ dotctrl --help
```

## Saving and Clone your dotfiles through Github (bonus)

Now that you have control of your dotfiles, it's time to save them. This example below will show you how to save to Github and performing clone.

1 - **Save:**

A - Entering the master dotfiles folder:

Linux:

```shell
$ cd /home/.dotfiles
```

macOS:

```shell
$ cd /Users/.dotfiles
```

B - Creating git repository, commit and saving (push)

```shell
$ git remote add origin git@github.com:<YOUR USER>/dotfiles.git
$ git init
$ git add .
$ git commit -m "Update"
$ git push origin main
```

2 - **Clone:**

You can clone any directory of your choice as well, but let's keep the example build directory above. Follow the steps:

Linux:

```shell
$ sudo mkdir /home/.dotfiles
$ sudo chmod 770 -R /home/.dotfiles
$ git clone git@github.com:<YOUR USER>/dotfiles.git /home/.dotfiles
$ cd /home/.dotfiles/linux
$ dotctrl link --force
```

macOS:

```shell
$ sudo mkdir /Users/.dotfiles
$ sudo chmod 770 -R /Users/.dotfiles
$ git clone git@github.com:<YOUR USER>/dotfiles.git /Users/.dotfiles
$ cd /home/.dotfiles/macos
$ dotctrl link --force
```

## Donation

Click on the image below to be redirected the donation forms:

<div class="donate">
  <a href="https://github.com/snakypy/donations/blob/master/README.md">
    <img width="160" height="100" src="https://raw.githubusercontent.com/snakypy/donations/master/svg/donate/donate-hand.svg" alt="Donations"/>
  </a>
</div>

## License

The project is available as open source under the terms of the [MIT License](https://github.com/snakypy/zshpower/blob/master/LICENSE) ©

## Credits

See, [AUTHORS](https://github.com/snakypy/zshpower/blob/master/AUTHORS.rst).
