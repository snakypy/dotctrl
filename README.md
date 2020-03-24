<h1 align="center">
  <a href="https://github.com/snakypy/dotctrl">
    <img alt="ZSHPower" src="https://raw.githubusercontent.com/snakypy/snakypy-static/master/dotctrl/logo/png/dotctrl.png" width="auto">
  </a>
</h1>

![Python package](https://github.com/snakypy/dotctrl/workflows/Python%20package/badge.svg) [![Build Status](https://travis-ci.com/snakypy/dotctrl.svg?branch=master)](https://travis-ci.com/snakypy/dotctrl) [![Updates](https://pyup.io/repos/github/snakypy/dotctrl/shield.svg)](https://pyup.io/repos/github/snakypy/dotctrl/) [![Python 3](https://pyup.io/repos/github/snakypy/dotctrl/python-3-shield.svg)](https://pyup.io/repos/github/snakypy/dotctrl/) ![PyPI - Wheel](https://img.shields.io/pypi/wheel/dotctrl) ![PyPI](https://img.shields.io/pypi/v/dotctrl) ![PyPI - Implementation](https://img.shields.io/pypi/implementation/dotctrl) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) ![PyPI - Downloads](https://img.shields.io/pypi/dm/dotctrl) [![GitHub license](https://img.shields.io/github/license/snakypy/dotctrl)](https://github.com/snakypy/dotctrl/blob/master/LICENSE)

<div align="center">
  <h4>
    <a href="#features">Features</a> |
    <a href="#requirements">Requirements</a> |
    <a href="#installing">Installing</a> |
    <a href="#using">Using</a> |
    <a href="#configuration">Configuration</a> |
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

`Dotctrl` is a package for managing your dot files on Linux. `Dotctrl` works on top of a configuration file that contains the absolute paths of the place of origin of dotfiles.

## Features

* Automatically manages dotfiles ending with rc in the user's HOME;
* Automatically manages the main configuration files of the editors: Atom, Sublime Text, Visual Studio Code;
* The `Dotctrl` repository stores the same path structure as the configuration files with the user's HOME files;

## Requirements

To work correctly, you will first need:

- [`Python`](https://python.org) (v3.7 or recent);
- [`Pip`](https://pip.pypa.io/en/stable/) (v19.3 or recent) must be installed;
- One of that editor [vim](https://www.vim.org/), [nano](https://www.nano-editor.org/) or [emacs](https://www.gnu.org/software/emacs/) must be installed;


## Installing

**1** - It's time to install `Dotctrl`. To do this, do:

Globally:

```shell
# pip install dotctrl
```
or

```shell
$ sudo pip install dotctrl
```

For the user:

```shell
$ pip install dotctrl --user
```

> NOTE: If you are installing to the user's local environment, be sure to add the environment variables to the `zshrc` or `.bashrc` file.

## Using

After installing the package, you need to create the Dotctrl repository in an empty folder in the location of your choice. For example:

```shell
$ mkdir ~/Dotfiles; cd $_
$ dotctrl init
```

## Configuration

`Dotctrl` works on top of a configuration file created in the Dotctrl repository, which is the **dotctrl.toml** file.

You can open the `Dotctrl` configuration file in the terminal itself using the command:

```shel
$ dotctrl config --open
```

### Understanding each section  `dotctrl.toml`:

**Section `dotctrl`:**

```toml
[dotctrl]
elements = []
```
* **elements**: As the name says, "*elements*" will store the absolute path of the elements you want to place inside the `Dotctrl` repository in a **list**. Examples:

```toml
elements = [".config/foo/foo.conf",
            ".config/bar/bar.conf",
            ".foo.conf"]
```

The `elements` option also accepts complete folders instead of just files:

```toml
elements = [".config/foo",
            ".config/bar"]
```

For madness but true, `Dotctrl` also manages files and folders without points:

```toml
elements = ["Documents/foo.txt",
            "Images/bar.jpg"]
```

You must place files (<u>or folders</u>) that are inside the user's **HOME**, as this is how `Dotctrl` works, only with elements in the user's HOME.



**Section `dotctrl.smart`:**

This section is very cool. It is the smart section of `Dotctrl`, where you will find configuration files and dotfiles for certain applications. :)

```toml
[dotctrl.smart]
rc.enable = true
text_editors.enable = true
```

* **rc.enable:** Option: `true`|`false`. If this option is `true`, ` Dotctrl` will search for all dotfiles in the user's *HOME* directory containing *rc* at the end. `Default:`*true*
* **text_editors.enable:** Option: `true`|`false`. If this option is `true`, ` Dotctrl` will search for the main dotfiles of the following text editors: [Atom](https://atom.io), [Sublime Text](https://www.sublimetext.com/), and [Visual Studio Code](https://code.visualstudio.com/).

## Upgrading

If `Dotctrl` has any new features, please update the command line below:

Globally:

```shell
# pip install dotctrl -U
```

or

```shell
$ sudo pip install dotctrl -U
```
For the user:

```shell
$ pip install dotctrl -U --user
```

## More Commands

For more command information, use:

```
$ dotctrl --help
```

## Donation

If you liked my work, buy me a coffee :coffee: :smiley:

[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=YBK2HEEYG8V5W&source)

## License

The project is available as open source under the terms of the [MIT License](https://github.com/snakypy/zshpower/blob/master/LICENSE) ©

## Credits

See, [AUTHORS](https://github.com/snakypy/zshpower/blob/master/AUTHORS.rst).
