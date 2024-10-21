import keyboard
from time import sleep

def main() -> None:
    keys = {
        "w": "up",
        "s": "down",
        "a": "left",
        "d": "right",
        "m": "z",
        "n": "x"
    }

    for key, rebind in keys.items():
        keyboard.on_press_key(key, lambda event, rebind=rebind: keyboard.press(rebind), suppress=True)
        keyboard.on_release_key(key, lambda event, rebind=rebind: keyboard.release(rebind), suppress=True)

    while not keyboard.is_pressed("shift"):
        sleep(0.5)

if __name__ == "__main__":
    main()