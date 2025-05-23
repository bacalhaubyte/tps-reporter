# About
TPS Reporter is a simple script with a boring name used to keep your computer from going to sleep or avoid appearing idle on popular messaging apps like Microsoft Teams, Slack, and others. Two scripts are included – one simulates mouse movements and the other keyboard presses (best for Microsoft Teams and generally recommended as it runs unobtrusively in the background). 

# Setup note for the non-technical
To use these scripts, you’ll need to have **Python** installed on your computer. Get it here: https://www.python.org/downloads/ 

Additionally, you must import one of two *libraries* referenced by the scripts: `pyautogui` if using the mouse script or `keyboard` if using the keyboard script. These can be quickly installed from the system terminal using the `pip` command.  
* Example:  `pip install keyboard`
* Example:  `pip install pyautogui`

Once Python and the required library are installed, you can easily run the script from the terminal (Linux) or PowerShell (Windows). Use `CD` to navigate to the folder where you saved the scripts and run them with python. If `.py` files are associated with Python on your computer, you can simply double click to run them.
* Example:  `CD Downloads`
* Example:  `python tpsreporter_keyboard.py`
