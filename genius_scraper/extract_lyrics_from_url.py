from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from .accept_cookies import accept_cookies
from genius_scraper import configs


def extract_lyrics_from_url(url, driver):
    try:
        # Visit the song URL
        driver.get(url)

        # Find all divs with the attribute data-lyrics-container="true"
        lyrics_containers = driver.find_elements(
            By.CSS_SELECTOR, 'div[data-lyrics-container="true"]')

        # Extract text from each container and join them
        lyrics = "\n".join(
            container.text for container in lyrics_containers)

        return lyrics

    except Exception as e:
        print(f"An error occurred: {e}")
        return None
