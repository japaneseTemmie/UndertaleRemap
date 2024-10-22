Simple undertale remap script.

- Adds W, A, S, D controls instead of arrow keys.
- Also remaps Z and X to M and N

To add custom keymaps simply edit the dictionary accordingly.
For example:
keys = {
    # New key "w": "up" # Key to be remapped
}

Dependencies:
keyboard module: pip install keyboard

Works both on Windows and Linux (requires sudo)
to run it on Windows with Python already installed, open a CMD window and type:

python path\to\main.py

to run it on Linux:

sudo python3 path/to/main.py

if you're using a venv change the python3 to the path of the interpreter in the venv.
