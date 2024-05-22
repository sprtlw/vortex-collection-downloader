import time
import pyautogui
import logging

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load button images
VORTEX_BUTTON_IMAGE = "vortex.png"


def configure_chrome_driver():
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

    driver = webdriver.Chrome(options=chrome_options)

    logger.info("Chrome driver configured with debugger address.")

    return driver


def wait_for_and_click_image(image_path, confidence=0.8, timeout=30):
    start_time = time.time()

    while time.time() - start_time < timeout:
        try:
            location = pyautogui.locateCenterOnScreen(
                image_path, confidence=confidence)

            if location is not None:
                pyautogui.click(location)
                logger.info(f"Clicked on image: {image_path}")

                return True
        except pyautogui.ImageNotFoundException:
            pass

        time.sleep(1)

    logger.warning(f"Image {image_path} not found within {timeout} seconds.")

    return False


def wait_for_new_tab(driver, timeout=10):
    start_time = time.time()
    initial_tabs = driver.window_handles

    while time.time() - start_time < timeout:
        current_tabs = driver.window_handles

        if len(current_tabs) > len(initial_tabs):
            return True

        time.sleep(1)
    return False


def click_web_download_buttons(driver):
    try:
        if not wait_for_new_tab(driver):
            raise Exception("No new tab opened.")

        driver.switch_to.window(driver.window_handles[-1])
        slow_download_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "slowDownloadButton"))
        )

        slow_download_button.click()

        logger.info("Clicked slow download button.")

        time.sleep(3)

        close_extra_tabs(driver)

        return True
    except Exception as e:
        logger.error(f"Error clicking slow download button: {e}")
        close_extra_tabs(driver)

        return False


def close_extra_tabs(driver):
    try:
        while len(driver.window_handles) > 1:
            driver.close()
            driver.switch_to.window(driver.window_handles[0])

        logger.info("Closed extra tabs.")
    except Exception as e:
        logger.error(f"Error closing extra tabs: {e}")


def main():
    driver = configure_chrome_driver()

    driver.get("https://www.google.com")

    try:
        while True:
            if wait_for_and_click_image(VORTEX_BUTTON_IMAGE):
                if not click_web_download_buttons(driver):
                    logger.warning("Retrying the process due to an error.")
                else:
                    logger.info("Successfully handled the web download.")
            else:
                logger.info(
                    "Waiting for the download button to appear on the screen...")
    finally:
        driver.quit()

        logger.info("Driver quit.")


if __name__ == "__main__":
    main()
