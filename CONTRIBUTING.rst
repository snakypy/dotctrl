============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every little bit
helps, and credit will always be given.

You can contribute in many ways:

Types of Contributions
----------------------

Report Bugs
~~~~~~~~~~~

Report bugs at https://github.com/snakypy/dotctrl/issues.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

Fix Bugs
~~~~~~~~

Look through the GitHub issues for bugs. Anything tagged with "bug" and "help
wanted" is open to whoever wants to implement it.

Implement Features
~~~~~~~~~~~~~~~~~~

Look through the GitHub issues for features. Anything tagged with "enhancement"
and "help wanted" is open to whoever wants to implement it.

Write Documentation
~~~~~~~~~~~~~~~~~~~

Dotctrl could always use more documentation, whether as part of the
official Dotctrl docs, in docstrings, or even on the web in blog posts,
articles, and such.

Submit Feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at https://github.com/dotctrl/dotctrl/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

Get Started!
------------

Ready to contribute? Here's how to set up `dotctrl` for local development.

1. Fork the `dotctrl` repo on GitHub.
2. Clone your fork locally:

    $ git clone git@github.com:your_name_here/dotctrl.git

3. Install your local copy on a virtualenv. Assuming you have poetry installed, this is how you set up your fork for local development:

    $ cd dotctrl/
    $ poetry shell
    $ poetry install

4. Create a branch for local development:

    $ git checkout -b name-of-your-bugfix-or-feature

   Now you can make your changes locally.

5. When you're done making changes, check that your changes pass flake8, black and the
   tests:

    $ poetry run tox


6. Commit your changes and push your branch to GitHub:

    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature

7. Submit a pull request through the GitHub website.

Pull Request Guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. The pull request should work for Python 3.8, and for PyPy. Check
   https://travis-ci.com/snakypy/dotctrl/pull_requests
   and make sure that the tests pass for all supported Python versions.


Developing with Docker
----------------------

The Dotctrl project contains Dockerfile, so you can see how the development is going using a Python image.

To do this, do:

1 - Build:

    $ docker build -t dotctrl:<version> .

2 - Access Dotctrl container in mode interactive:

    $ docker run --rm -it dotctrl:<version>

3 - Run the "docker.sh" script to create the Dotctrl repository:

    $ ./docker.sh

Appear in credits
------------------

If you contribute over 100 lines of code to the project, your name and some of your data will appear in the Dotctrl credits when run the command:

    $ dotctrl --credits

Not only that, but your name will also appear in AUTHORS.rst. How about, huh?