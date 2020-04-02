.. image:: https://raw.githubusercontent.com/snakypy/snakypy-static/master/dotctrl/logo/png/dotctrl.png
    :width: 441 px
    :align: center
    :alt: Dotctrl


.. image:: https://github.com/snakypy/dotctrl/workflows/Python%20package/badge.svg
    :target: https://github.com/snakypy/dotctrl

.. image:: https://img.shields.io/pypi/v/dotctrl.svg
    :target: https://pypi.python.org/pypi/dotctrl

.. image:: https://travis-ci.com/snakypy/dotctrl.svg?branch=master
    :target: https://travis-ci.com/snakypy/dotctrl

.. image:: https://img.shields.io/pypi/wheel/dotctrl
    :alt: PyPI - Wheel

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black

.. image:: https://pyup.io/repos/github/snakypy/dotctrl/shield.svg
    :target: https://pyup.io/repos/github/snakypy/dotctrl
    :alt: Updates

.. image:: https://img.shields.io/github/issues-raw/snakypy/dotctrl
    :alt: GitHub issues

.. image:: https://img.shields.io/github/license/snakypy/dotctrl
    :alt: GitHub license
    :target: https://github.com/snakypy/dotctrl/blob/master/LICENSE


`Dotctrl` is a package for managing your "dotfiles" on Linux. `Dotctrl` works on top of a configuration file that contains the absolute paths of the place of origin of dotfiles.

Features
--------

* Automatically manages dotfiles ending with rc in the user's HOME;
* Automatically manages the main configuration files of the editors: Atom, Sublime Text, Visual Studio Code;
* The `Dotctrl` repository stores the same path structure as the configuration files with the user's HOME files;

Requirements
------------

To work correctly, you will first need:

* `python`_ (v3.8 or recent) must be installed.
* `pip`_ (v19.3 or recent) must be installed.

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

If you liked my work, buy me a coffee <3

.. image:: https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif
    :target: https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=YBK2HEEYG8V5W&source

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
.. _MIT License: https://github.com/snakypy/dotctrl/blob/master/LICENSE
.. _William Canin: http://williamcanin.github.io
