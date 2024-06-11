from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from .accept_cookies import accept_cookies
from genius_scraper import configs


def extract_all_songs(url):
    # Chrome Browser setup
    driver = webdriver.Chrome(service=Service(
        configs.chromedriver_path), options=configs.chrome_options)

    print("Initiating songs extraction process")

    # Open the URL
    driver.get(url)

    print("Successfully loaded the webpage")

    accept_cookies(driver)

    # Initialize an empty list to store links
    links = []

    # Initialize variables to track the last song title
    last_song_title = ""

    print("Scrolling through all songs")

    while True:
        # Extract song links and titles
        ul_element = driver.find_element(
            By.CLASS_NAME, 'ListSectiondesktop__Items-sc-53xokv-8.kbIuNQ')
        li_elements = ul_element.find_elements(
            By.CLASS_NAME, 'ListItem__Container-sc-122yj9e-0.eRBVjI')

        # Check if the last song title is the same after scrolling
        current_last_song_title = li_elements[-1].find_element(
            By.CLASS_NAME, 'ListItem__Title-sc-122yj9e-4.nknYf').text.strip()
        if current_last_song_title == last_song_title:
            break
        last_song_title = current_last_song_title

        # Scroll to the last <li> element
        driver.execute_script(
            "arguments[0].scrollIntoView();", li_elements[-1])

        # Wait to load page
        time.sleep(3)

    print("Finished scrolling")

    # Extract song links and titles after scrolling is complete
    ul_element = driver.find_element(
        By.CLASS_NAME, 'ListSectiondesktop__Items-sc-53xokv-8.kbIuNQ')
    li_elements = ul_element.find_elements(
        By.CLASS_NAME, 'ListItem__Container-sc-122yj9e-0.eRBVjI')

    for li in li_elements:
        a_tag = li.find_element(
            By.CLASS_NAME, 'ListItem__Link-sc-122yj9e-1.klWOzg')
        h3_tag = li.find_element(
            By.CLASS_NAME, 'ListItem__Title-sc-122yj9e-4.nknYf')
        link = a_tag.get_attribute('href')
        title = h3_tag.text.strip()
        links.append((title, link))

    print(f"Retrieved {len(links)} songs")

    # Close the driver
    driver.quit()

    return links
