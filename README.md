# Add shebang to python files

<!--- These are examples. See https://shields.io for others or to customize this set of shields. You might want to include dependencies, project status and licence info here --->

![GitHub repo size](https://img.shields.io/github/repo-size/richardnilsson/add_python_shebang)
![GitHub contributors](https://img.shields.io/github/contributors/richardnilsson/add_python_shebang)
![GitHub stars](https://img.shields.io/github/stars/richardnilsson/add_python_shebang?style=social)
![GitHub forks](https://img.shields.io/github/forks/richardnilsson/add_python_shebang?style=social)

<!-- ![Twitter Follow](https://img.shields.io/twitter/follow/scottydocs?style=social) -->

Add shebang to python files is a `utility` that allows `python developers` to `add a shebang` to their Python files.

This script can be used to add a `shebang` to a python file, and also a `Module Docstring` and `if __name__ == '__main__'` to empty Python files.
Personally I use it in `vscode` with [Run on Save](https://marketplace.visualstudio.com/items?itemName=pucelle.run-on-save).

<!-- ## Prerequisites

Before you begin, ensure you have met the following requirements:

<!--- These are just example requirements. Add, duplicate or remove as required --->

<!-- - You have installed the latest version of `<coding_language/dependency/requirement_1>`
- You have a `<Windows/Linux/Mac>` machine. State which OS is supported/which is not.
- You have read `<guide/link/documentation_related_to_project>`.  -->

## Installing add shebang to python files

To install add shebang to python files, follow these steps:

Linux and macOS:

- Clone this repo
- Copy `add_shebang_cli.py` to your `PATH`
- Make `add_shebang_cli.py` executable with `chmod +x add_shebang_cli.py`

<!--
```bash
<install_command>
``` -->

<!-- Windows:

```powershell
<install_command>
``` -->

## Using add shebang to python files

To use add shebang to python files, follow these steps:

- Add the following lines in `settings.json` in `vscode`:

```json
    "runOnSave.commands": [
        {
            "match": ".*\\.py$",
            "command": "add_shebang_cli.py ${file}",
            "runIn": "backend"
        }
    ]
```

Your python files will now be checked for shebang and if it's not present it will be added.

[![asciicast](https://asciinema.org/a/ECSFeaqLeLtdnRovJbDyDXuCV.svg)](https://asciinema.org/a/ECSFeaqLeLtdnRovJbDyDXuCV)

<!-- ```bash
<usage_example>
``` -->

Add run commands and examples you think users will find useful. Provide an options reference for bonus points!

## Contributing to add shebang to python files

<!--- If your README is long or you have some specific process or steps you want contributors to follow, consider creating a separate CONTRIBUTING.md file--->

To contribute to add shebang to python files, follow these steps:

1. Fork this repository.
2. Create a branch: `git checkout -b <branch_name>`.
3. Make your changes and commit them: `git commit -m '<commit_message>'`
4. Push to the original branch: `git push origin <project_name>/<location>`
5. Create the pull request.

Alternatively see the GitHub documentation on [creating a pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

<!-- ## Contributors

Thanks to the following people who have contributed to this project:

- [@scottydocs](https://github.com/scottydocs) 📖
- [@cainwatson](https://github.com/cainwatson) 🐛
- [@calchuchesta](https://github.com/calchuchesta) 🐛

You might want to consider using something like the [All Contributors](https://github.com/all-contributors/all-contributors) specification and its [emoji key](https://allcontributors.org/docs/en/emoji-key).

## Contact

If you want to contact me you can reach me at <your_email@address.com>. -->

## License

<!--- If you're not sure which open license to use see https://choosealicense.com/--->

This project uses the following license: [MIT License](https://choosealicense.com/licenses/mit/#).
