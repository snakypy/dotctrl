from dotctrl.config import package

content = f"""# {package.info['name']}

> NOTE: This is an informational README only.

## About

**Brief description:**

All *dotfiles* files are kept in the **dotctrl** repository/folder.
Depending on what you add to the configuration file (`{package.info['config']}`),
many will be stored in the repository with a dot (.) to maintain compatibility with
directories and files on your machine's drive, that is, all paths of the
repository **dotctrl**, are compatible with those belonging to the **$HOME**.

## Inspection

To view the dot files in the `dotctrl` repository, activate the option to view
hidden files in the file manager of your Linux distribution.

To check the files via the command line, do:

```shell
$ du -a ./dotctrl | more
```

## Management

These *dotfiles* were generated with the \
[**Dotctrl**]({package.info['home_page']}) package.
To use, allow yourself to [visit the project]({package.info['home_page']})
repository and read its functionality.

---
Offered by: [`Snakypy Organization`](https://github.com/snakypy).
"""
