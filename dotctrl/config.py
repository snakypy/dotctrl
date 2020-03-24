from datetime import datetime
from dotctrl import __version__, __pkginfo__

config_rc_content = f"""# << {__pkginfo__['name']} configuration >>
# Datetime: {datetime.today().isoformat()}
# Version: {__version__}
# -----------------------------------------------------
# For more information, see: {__pkginfo__['home_page']}#configuration

[dotctrl]
elements = []

[dotctrl.smart]
rc.enable = true
text_editors.enable = true
"""

gitignore_content = f"""# {__pkginfo__['name']}: Ignored by default.

__pycache__/
*.lock
*.log
*.egg
*.so
.cache
"""

readme_content = f"""# {__pkginfo__['name']}

> NOTE: This is an informational README only.

## About

**Brief description:**

All *dotfiles* files are kept in the **dotctrl** repository/folder.
Depending on what you add to the configuration file (`dotctrl.toml`), many will be
stored in the repository with a dot (.) to maintain compatibility with directories
and files on your machine's drive, that is, all files and paths of the repository
**dotctrl**, are compatible with those belonging to the **$HOME**.

## Inspection

To view the dot files in the `dotctrl` repository, activate the option to view
hidden files in the file manager of your Linux distribution.

To check the files via the command line, do:

```shell
$ du -a ./dotctrl | more
```

## Management

These *dotfiles* were generated with the \
[**Dotctrl**]({__pkginfo__['home_page']}) package.
To use, allow yourself to [visit the project]({__pkginfo__['home_page']})
repository and read its functionality.

---
Offered by: [`Snakypy Organization`](https://github.com/snakypy).
"""
