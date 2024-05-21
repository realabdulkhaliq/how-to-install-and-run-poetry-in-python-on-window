# how-to-install-and-run-poetry-in-python-on-window

## How to Install/Uninstall and Run Poetry in Python on Window

1. Run the following command in Windows PowerShell

```
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

**Note:** _If you've installed Python through the Microsoft Store, replace py with python in the command_

2. Wait for the Installation. After installation complete add the provided (provided after installaion on PowerShell) Path to Environment Variables

3. Close PowerShell and Re-open againg and run
   `poetry --version`

4. If you want to uninstall poetry again then use uninstall flag

```
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python - --uninstall
```
