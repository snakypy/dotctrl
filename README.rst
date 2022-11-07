.. image:: https://raw.githubusercontent.com/snakypy/assets/main/dotctrl/images/dotctrl-transparent.png
    :width: 441 px
    :align: center
    :alt: Dotctrl

_________________

.. image:: https://github.com/snakypy/dotctrl/workflows/Tests/badge.svg
    :target: https://github.com/snakypy/dotctrl
    :alt: Tests

.. image:: https://img.shields.io/pypi/v/dotctrl.svg
    :target: https://pypi.python.org/pypi/dotctrl
    :alt: PyPI - Dotctrl

.. image:: https://img.shields.io/pypi/wheel/dotctrl
    :target: https://pypi.org/project/wheel/
    :alt: PyPI - Wheel

.. image:: https://img.shields.io/pypi/pyversions/dotctrl
    :target: https://pyup.io/repos/github/snakypy/dotctrl/
    :alt: Python versions

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
    :alt: Black

.. image:: https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336
    :target: https://pycqa.github.io/isort/
    :alt: Isort

.. image:: http://www.mypy-lang.org/static/mypy_badge.svg
    :target: http://mypy-lang.org/
    :alt: Mypy

.. image:: https://pyup.io/repos/github/snakypy/dotctrl/shield.svg
   :target: https://pyup.io/repos/github/snakypy/dotctrl/
   :alt: Updates

.. image:: https://img.shields.io/github/issues-raw/snakypy/dotctrl
   :target: https://github.com/snakypy/dotctrl/issues
   :alt: GitHub issues

.. image:: https://img.shields.io/github/license/snakypy/dotctrl
    :alt: GitHub license
    :target: https://github.com/snakypy/dotctrl/blob/master/LICENSE

_________________

Initially, `Dotctrl` was created just to control "dotfiles files", however, in the course, it became more than that.
`Dotctrl` is now a maintainer of any file and folder type within its own private repository.

This is too much!

`Dotctrl` will manage the elements of the user's HOME directory; running on top of a configuration file (`dotctrl.json`)
that contains the paths to the origin location of the elements.

All elements managed by `Dotctrl` are kept in the repository/folder "`dotctrl`".

Features
--------

* Language support: American English and Brazilian Portuguese;
* Create (or not) multiple repositories for your elements;
* Abandon the creation of huge manual symlinks;
* O armazenará a mesma estrutura de caminho que seu local (`$HOME`) original;
* Manage single or bulk elements;
* Restore repository elements to their original location with a single command;
* And much more :)

Requirements
------------

To work correctly, you will first need:

* Linux or macOS.
* `python`_ (v3.9 or recent) must be installed.
* `pip`_ (v19.3 or recent) must be installed.
* `git`_ (v2.0 or recent) must be installed.

Installing
----------

.. code-block:: shell

    $ python3 -m pip install dotctrl --user


Using
-----

To know the commands of `Dotctrl`, run the command:

.. code-block:: shell

    $ dotctrl -h

Also visit the Dotctrl `home page`_ and see more about settings and usability.

Links
-----

* Code: https://github.com/snakypy/dotctrl
* Documentation: https://github.com/snakypy/dotctrl/blob/main/README.md
* Releases: https://pypi.org/project/dotctrl/#history
* Issue tracker: https://github.com/snakypy/dotctrl/issues

Donation
--------

Click on the image below to be redirected the donation forms:

.. image:: https://raw.githubusercontent.com/snakypy/donations/main/svg/donate/donate-hand.svg
    :width: 160 px
    :height: 100px
    :target: https://github.com/snakypy/donations/blob/main/README.md

License
-------

The gem is available as open source under the terms of the `MIT License`_ ©

Credits
-------

See, `AUTHORS`_.

.. _`AUTHORS`: https://github.com/snakypy/dotctrl/blob/main/AUTHORS.rst
.. _`home page`: https://github.com/snakypy/dotctrl
.. _`python`: https://python.org
.. _pip: https://pip.pypa.io/en/stable/quickstart/
.. _git: https://git-scm.com/downloads
.. _MIT License: https://github.com/snakypy/dotctrl/blob/main/LICENSE
.. _William Canin: http://williamcanin.github.io
