# Vortex Collection Downloader Script

This script automates the process of installing Nexus Mods collections through Vortex using PyAutoGUI and handling the web downloading with Selenium.

## Requirements
- Google Chrome browser
- ChromeDriver compatible with your Chrome version
- Python

## Setup

### Install Required Libraries

Install the required libraries:
```
pip install -r requirements.txt
```

### Open Chrome in Debugging Mode via cmd (Replace USER with windows username)

Chrome:
```
chrome.exe --remote-debugging-port=9222 --user-data-dir="C:/Users/USER/AppData/Local/Google/Chrome/User Data"
```

### Open Vortex

Ensure both vortex and chrome are visible. Start collection download and run the script once you see the orange download button.

### Run the Script

Python:
python app.py
