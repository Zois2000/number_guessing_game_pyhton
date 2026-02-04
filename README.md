
# Number Guessing Game (Python)

## Run (Windows / PowerShell)

PowerShell does **not** automatically execute `.py` files unless you have a file association set up. That's why running:

`./src/__main__.py`

can appear to "do nothing".

Use one of these instead:

### Option A (recommended): run as a module

`./.venv/Scripts/python.exe -m src`

### Option B: run the file explicitly with Python

`./.venv/Scripts/python.exe ./src/__main__.py`

### Option C: helper script

`./run.ps1`

