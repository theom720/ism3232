# ISM3232 — Module 2: zsh Navigation and File Operations

## Commands Practiced

| Command         | What it does                                         |
|-----------------|---------------------------------------------------   |
| pwd             | Prints the current working directory (absolute path) |
| ls              | Lists visible files and folders                      |
| ls -la          | Lists all files including hidden ones, long format   |
| cd Documents    | Enters a folder using a relative path                |
| cd ..           | Moves up one directory level                         |
| cd ~            | Jumps to the home directory from anywhere            |
| cd ~/ism3232    | Goes to the course folder via a path from home       |
| mkdir           | Creates a new directory                              |
| mkdir -p        | Creates nested directories, making parents as needed |
| touch           | Creates an empty file (or updates its timestamp)     |
| echo 'x' > f    | Writes text to a file, overwriting it                |
| cat             | Prints the entire contents of a file                 |
| head -5         | Shows the first 5 lines of a file                    |
| tail -5         | Shows the last 5 lines of a file                     |
| less            | Opens a scrollable view of a file (q to quit)        |
| cp              | Copies a file; the original stays in place           |
| mv              | Moves or renames a file; the original is gone        |
| rm              | Permanently deletes a file — no trash, no undo       |
| rm -r           | Deletes a folder and its contents recursively        |
| tree -L 2       | Shows the directory structure, 2 levels deep         |
| clear           | Clears the terminal screen                           |
| code .          | Opens the current folder as a VS Code workspace      |

## AI Use Statement
I did not use AI for this lab.

## Week 3: Virtual Environments and .zshrc

- `python3 -m venv .venv` - create an isolated virtual environment
- `source .venv/bin/activate` - activate it; prompt shows (.venv)
- `which python3` - verify active Python points inside .venv/bin/
- `pip install pytest ruff` - install packages into the venv only
- `pip freeze > requirements.txt` - snapshot pinned versions
- `pip install -r requirements.txt` - recreate the env elsewhere
- `deactivate` - leave the venv, back to system Python

### Aliases added to ~/.zshrc
- `ll` → `ls -la`
- `c` → `clear`
- `py` → `python3`
- `gs` → `git status`
- `ga` → `git add .`
- `gcmsg` → `git commit -m`
- `gp` → `git push`
- `gl` → `git log --oneline`
- `tree2` → `tree -L 2`
- `mkcd <dir>` → make a folder and cd into it