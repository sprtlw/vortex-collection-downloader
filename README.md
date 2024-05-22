# Vortex Collection Downloader Script

This script automates the process of installing Nexus Mods collections through Vortex using PyAutoGUI and handling the web downloading with Selenium.

## Requirements
- Google Chrome browser
- ChromeDriver compatible with your Chrome version
- Python
- FastForward (skip wait time): https://fastforward.team

## Setup

### Install Required Libraries

Pip:
```
pip install -r requirements.txt
```

### Open Chrome in Debugging Mode via cmd (Replace USER with windows username)

Chrome:
```
"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:/Users/USER/AppData/Local/Google/Chrome/User Data"
```

### Open Vortex

Ensure both vortex and chrome are visible. Start collection download and run the script once you see the orange download button.

### Run the Script

Python:
```
python app.py
```

## Contributing
Feel free to submit pull requests or open issues if you encounter any problems or have suggestions for improvements.

## License
This project is licensed under the MIT License.
