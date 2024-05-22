import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Load button images
vortex_button_image = "vortex.png"

# Configure Selenium to use an existing Chrome session
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

# Initialize the WebDriver (assuming you're using Chrome)
driver = webdriver.Chrome(options=chrome_options)


def wait_for_and_click_image(image_path):
    while True:
        try:
            location = pyautogui.locateCenterOnScreen(
                image_path, confidence=0.8)
            if location is not None:
                pyautogui.click(location)
                return True
        except pyautogui.ImageNotFoundException:
            pass
        time.sleep(1)  # Sleep for a short period before checking again


def click_web_download_buttons():
    try:
        # Switch to the new window opened
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[-1])

        # Find and click the grey "Slow Download" button by its ID
        slow_download_button = driver.find_element(By.ID, "slowDownloadButton")
        slow_download_button.click()

        # Wait for 3 seconds before closing the tab
        time.sleep(3)

        # Check if there's more than one tab before closing
        if len(driver.window_handles) > 1:
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
        return True
    except Exception as e:
        print("Error clicking slow download button:", e)
        try:
            # Only attempt to close the tab if there's more than one
            if len(driver.window_handles) > 1:
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
        except Exception as inner_e:
            print("Error switching back to the main window:", inner_e)
        return False


# Open a placeholder page to initialize the driver
driver.get("https://www.google.com")

try:
    while True:
        if wait_for_and_click_image(vortex_button_image):
            if not click_web_download_buttons():
                print("Retrying the process due to an error.")
            else:
                print("Successfully handled the web download.")
        else:
            print("Waiting for the download button to appear on the screen...")
finally:
    # Close the driver at the end of the script
    driver.quit()
