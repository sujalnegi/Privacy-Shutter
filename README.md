
# Privacy Shutter
  
**Your instant escape button that helps you to escape tricky situations**

Privacy Shutter is a minimalist USB HID tool for the PicoDucky (CircuitPython). When activated, it instantly minimizes all windows and performs a pre-defined key sequence to quickly hide current activity, acting as your personal, undetectable digital panic button.

[![Python 3.19.9](https://img.shields.io/badge/python-3.19.9-blue.svg)](https://www.python.org/downloads/release/python-31210/)
[![GitHub Repo](https://img.shields.io/badge/GitHub-Privacy_Shutter-purple?logo=github)](https://github.com/sujalnegi/Privacy-Shutter)
[![Built for PicoDucky](https://img.shields.io/badge/Built%20for-PicoDucky-purple)](https://picoducky.hackclub.com/)


## Demo Video

Demo video for no pico script [here](https://drive.google.com/file/d/1nOX7HdE5QQOwLlq48w09lEvt4-07vOx8/view?usp=drive_link)

Demo for pico script (main.py) [Soon!]()



## **Scripts**
### No Pico

**Flow of Script**
- Prep: Wait 2 seconds.
- Minimize: Minimize all open windows.
- Launch Spotify: Open the Spotify application.
- Launch VS Code: Open the Visual Studio Code editor.
- Open LeetCode: Execute a command to open the LeetCode URL in a browser.
- Switch Window: Use Alt + Tab to focus on the VS Code window.
- Tile Left: Snap VS Code to the left half of the screen.
- Tile Right: Press Enter to snap the LeetCode browser window to the right half.
- Finish: Print "Development environment setup complete!"

### Installation

**Step 1: Clone the Repository**
```bash
git clone [https://github.com/YourUsername/YourRepoName.git](https://github.com/YourUsername/YourRepoName.git)
cd "Privacy Shutter"
```
**Step 2: Install Dependencies**
```bash
pip install pyautogui
```
**Step 3: Configure Applications (Optional)**

The script relies on exact application names for the Windows Start Menu search.

- The script tries to launch "spotify" and "vscode".

- If your system uses a different name (e.g., "Visual Studio Code"), you must edit the application names within the main function of the Python file to match your system.

**Step 4: Run the Script**

Execute the script from your terminal:

```bash
python no_picoducky_main.py
```

## Author

- Email: [sujal1negi@gmail.com](mailto:sujal1negi@gmail.com)
- Instagram: [@_sujal1negi_](https://www.instagram.com/_sujalnegi_/)
