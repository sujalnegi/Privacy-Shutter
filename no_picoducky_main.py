import time
import pyautogui

def press_keys(*keys, delay=0.1):
    pyautogui.hotkey(*keys)
    time.sleep(delay)

def type_text(text, delay=0.05):
    pyautogui.write(text, interval=delay)
    time.sleep(delay)

def minimize_all_windows():
    print("Minimizing all windows...")
    press_keys('win', 'd')
    time.sleep(1)

def launch_application(app_name):
    print(f"Launching {app_name}...")
    press_keys('win') 
    time.sleep(0.8) 
    type_text(app_name)
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(4) 

def open_browser_url_via_cmd(url):
    print(f"Opening {url} via Command Prompt...")
    
    press_keys('win')
    time.sleep(0.5)

    type_text("cmd")
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(1)

    # Use '&& exit' to run the start command and then immediately close CMD
    command = f"start http://{url} && exit\n"
    type_text(command)
    time.sleep(5) 

def tile_window_left():
    print("Tiling window to left...")
    press_keys('win', 'left')
    time.sleep(0.8)

def tile_window_right():
    print("Tiling window to right...")
    press_keys('win', 'right')
    time.sleep(0.8)

# def switch_to_next_window():
#     """Switch to next window (Alt+Tab on Windows)"""
#     print("Switching to next window...")
#     press_keys('alt', 'tab')
#     time.sleep(0.5)

def main():
    print("Starting development environment setup...")
    time.sleep(2)
    
    minimize_all_windows()
    
    launch_application("spotify")
    
    launch_application("vscode")
    
    open_browser_url_via_cmd("leetcode.com/problemset/")
    
    print("\n=== Optional Window Tiling ===")
    
    # Switch to VS Code (Alt+Tab once switches to the previously focused window)
    time.sleep(1)
    press_keys('alt', 'tab')
    time.sleep(0.5)
    
    # Tile VS Code to left
    tile_window_left()
    
    # The browser window should now be offered as a snap option on the right.
    time.sleep(1)
    
    # Tile browser to right using the Windows auto-snap feature
    press_keys('enter')
    # if the automatic tiling feature is not in ur windows replace the above function with the function below
    # tile_window_right()
    
    print("\nDevelopment environment setup complete!")

if __name__ == "__main__":
    main()