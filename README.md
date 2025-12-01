# Simple UNDERTALE remap script.

- Adds W, A, S, D controls instead of arrow keys.
- Remaps Z and X to M and N

All original controls can still be used even if the script is active.

# Dependencies and running the script
Works both on Windows and Linux (requires sudo)

Install dependencies: `pip install -r requirements.txt`

To execute it on Windows with Python already installed, open a CMD window and type:

`python main.py`

to run it on Linux:

`sudo python3 main.py`

if you're using a venv, change the previous 'python3' to the path of the interpreter in the venv.

To exit the script, hold the SHIFT key.

# Extending the program

To add custom keymaps, simply edit the `keys` hashmap accordingly.

For example:

```python
keys = {
    "w": "up",
    "z": "m"
} # New key -> Key to be remapped
```
