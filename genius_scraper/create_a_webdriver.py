from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from genius_scraper import configs


def create_a_webdriver():
    # Chrome Browser setup
    driver = webdriver.Chrome(service=Service(
        configs.chromedriver_path), options=configs.chrome_options)

    return driver
