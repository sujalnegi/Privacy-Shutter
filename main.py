import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

def press_keys(*keys):
    # Press keys simultaneously
    kbd.press(*keys)
    time.sleep(0.1)
    kbd.release_all()
    time.sleep(0.2)

def type_text(text):
    # Type text string
    layout.write(text)
    time.sleep(0.05)

def minimize_all_windows():
    # Windows: Win + D
    press_keys(Keycode.GUI, Keycode.D)
    time.sleep(1)

def launch_application(app_name):
    # Open search (Windows Key)
    press_keys(Keycode.GUI)
    time.sleep(0.8)
    type_text(app_name)
    time.sleep(0.5)
    press_keys(Keycode.ENTER)
    time.sleep(4)

def open_browser_url_via_cmd(url):
    # 1. Open search
    press_keys(Keycode.GUI)
    time.sleep(0.5)

    # 2. Launch cmd
    type_text("cmd")
    time.sleep(0.5)
    press_keys(Keycode.ENTER)
    time.sleep(1)

    # 3. Use 'start' command to open URL and '&& exit' to close CMD
    command = f"start http://{url} && exit\n"
    type_text(command)
    time.sleep(5)

def tile_window_left():
    # Win + Left Arrow
    press_keys(Keycode.GUI, Keycode.LEFT_ARROW)
    time.sleep(0.8)


# not needed if windows auto tiling feature is actively running
# def tile_window_right():
#     # Win + Right Arrow
#     press_keys(Keycode.GUI, Keycode.RIGHT_ARROW)
#     time.sleep(0.8)

def main():
    # Wait for USB enumeration
    time.sleep(2)

    minimize_all_windows()

    launch_application("spotify")

    launch_application("vscode")

    open_browser_url_via_cmd("leetcode.com/problemset/")

    # Switch to VS Code (Alt+Tab to go to previous window)
    time.sleep(1)
    press_keys(Keycode.ALT, Keycode.TAB)
    time.sleep(0.5)

    # Tile VS Code to left
    tile_window_left()

    time.sleep(1)

    # Tile browser to right using Windows auto-snap feature (Enter key)
    press_keys(Keycode.ENTER)
    # If Windows auto-snap fails, replace the above line with:
    # tile_window_right()

if __name__ == "__main__":
    main()