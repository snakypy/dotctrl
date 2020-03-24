from setuptools import setup, find_packages
from os.path import dirname, abspath, join
from dotctrl import __name__, __pkginfo__, __version__


ROOT = dirname(abspath(__file__))

readme_rst = join(ROOT, "README.rst")
with open(readme_rst) as f:
    long_description = f.read()

requirements = join(ROOT, "requirements.txt")
with open(requirements) as f:
    install_requires = [i.strip().split("#", 1)[0].strip()
                        for i in f.read().strip().split('\n')]

requirements_dev = join(ROOT, "requirements_dev.txt")
extras_require = {}
with open(requirements_dev) as f:
    extras_require["dev"] = [i.strip().split("#", 1)[0].strip()
                             for i in f.read().strip().split('\n')]

# Variables setup
license_ = "MIT license",
license_classifiers = "License :: OSI Approved :: MIT License"
cli_exec = f"{__pkginfo__['executable']}={__name__}.cli:main"
# entry_points_line = {'console_scripts': [cli_exec]}

setup(
    name=__pkginfo__["pkg_name"],
    version=__version__,
    description=__pkginfo__["description"],
    author=__pkginfo__["author"]["name"],
    author_email=__pkginfo__["author"]["email"],
    license=license_,
    maintainer=__pkginfo__["author"]["name"],
    # Types: text/plain, text/x-rst, text/markdown
    long_description_content_type="text/x-rst",
    long_description=long_description,
    url=__pkginfo__["home_page"],
    packages=find_packages(include=["dotctrl",
                                    "dotctrl.*"]),
    install_requires=install_requires,
    scripts=[],
    # extras_require=extras_require,
    classifiers=["Intended Audience :: Developers",
                 license_classifiers,
                 "Operating System :: POSIX :: Linux",
                 "Operating System :: MacOS :: MacOS X",
                 "Operating System :: Unix",
                 "Programming Language :: Python :: 3"],
    python_requires=">= 3.8",
    keywords="DotCtrl dotctrl dotfiles linux manager dot python3",
    # entry_points=entry_points_line,
    entry_points=f"""
        [console_scripts]
            {cli_exec}
    """,
    package_data={
        "": ["LICENSE", "requirements_dev.txt", "CHANGELOG.rst"]}
)
