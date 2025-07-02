# Simple UNDERTALE remap script.

- Adds W, A, S, D controls instead of arrow keys.
- Remaps Z and X to M and N

# Extending the program

To add custom keymaps simply edit the hashmap accordingly.
For example:

`keys = {"w": "up", "z": "m"} # New key -> Key to be remapped`

# Dependencies
keyboard module: `pip install keyboard`

Works both on Windows and Linux (requires sudo)
To execute it on Windows with Python already installed, open a CMD window and type:

`python path\to\main.py`

to run it on ✨Linux✨:

`sudo python3 path/to/main.py`

if you're using a venv change the python3 to the path of the interpreter in the venv.
