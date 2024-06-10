from selenium.webdriver.common.by import By
import time


def accept_cookies(driver):
    # wait for cookie button to appear
    time.sleep(2)

    # Accept cookies if the button is present
    try:
        accept_button = driver.find_element(
            By.ID, 'onetrust-accept-btn-handler')
        accept_button.click()
        time.sleep(2)  # Wait for the click to register
        print("Accepted website cookies")

    except Exception as e:
        print("No cookies acceptance button found or an error occurred:", e)
