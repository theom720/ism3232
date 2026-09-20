## Week 3: Virtual Environments and .zshrc

- `python3 -m venv .venv` — create an isolated virtual environment
- `source .venv/bin/activate` — activate it; prompt shows (.venv)
- `which python3` — verify active Python points inside .venv/bin/
- `pip install pytest ruff` — install packages into the venv only
- `pip freeze > requirements.txt` — snapshot pinned versions
- `pip install -r requirements.txt` — recreate the env elsewhere
- `deactivate` — leave the venv, back to system Python

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