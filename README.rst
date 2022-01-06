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

`Dotctrl` is a package for managing your "dotfiles" on Linux or macOS. `Dotctrl` works on top of a configuration file that contains the absolute paths of the place of origin of dotfiles.

Features
--------

* Automatically manages dotfiles ending with rc in the user's HOME;
* Automatically manages the main configuration files of the editors: Atom, Sublime Text, Visual Studio Code;
* The `Dotctrl` repository stores the same path structure as the configuration files with the user's HOME files;

Requirements
------------

To work correctly, you will first need:

* `python`_ (v3.9 or recent) must be installed.
* `pip`_ (v19.3 or recent) must be installed.
* `git`_ (v2.0 or recent) must be installed.

Installing
----------

Globally:

.. code-block:: shell

    $ sudo pip install dotctrl

For the user:

.. code-block:: shell

    $ pip install dotctrl --user


Using
-----

To know the commands of `Dotctrl`, run the command:

.. code-block:: shell

    $ dotctrl -h

Also visit the Dotctrl `home page`_ and see more about settings and usability.

Links
-----

* Code: https://github.com/snakypy/dotctrl
* Documentation: https://github.com/snakypy/dotctrl/blob/master/README.md
* Releases: https://pypi.org/project/dotctrl/#history
* Issue tracker: https://github.com/snakypy/dotctrl/issues

Donation
--------

Click on the image below to be redirected the donation forms:

.. image:: https://raw.githubusercontent.com/snakypy/donations/master/svg/donate/donate-hand.svg
    :width: 160 px
    :height: 100px
    :target: https://github.com/snakypy/donations/blob/master/README.md

License
-------

The gem is available as open source under the terms of the `MIT License`_ ©

Credits
-------

See, `AUTHORS`_.

.. _`AUTHORS`: https://github.com/snakypy/dotctrl/blob/master/AUTHORS.rst
.. _`home page`: https://github.com/snakypy/dotctrl
.. _`python`: https://python.org
.. _pip: https://pip.pypa.io/en/stable/quickstart/
.. _git: https://git-scm.com/downloads
.. _MIT License: https://github.com/snakypy/dotctrl/blob/master/LICENSE
.. _William Canin: http://williamcanin.github.io
