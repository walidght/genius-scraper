from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from .accept_cookies import accept_cookies
from genius_scraper import configs


def get_artist_url(query):
    # Chrome Browser setup
    driver = webdriver.Chrome(service=Service(
        configs.chromedriver_path), options=configs.chrome_options)

    print("Initiating search process on Genius")

    try:
        # Open the URL
        driver.get("https://genius.com/")

        print("Successfully loaded the webpage")

        accept_cookies(driver)

        # Find the search input field
        search_input = driver.find_element(By.NAME, "q")

        print("Entering search query")

        # Input the search query and submit the form
        search_input.send_keys(query)
        search_input.submit()

        print("Search query submitted, awaiting results")

        # Wait for the search results page to load
        driver.implicitly_wait(10)

        # Find the container of top result
        container = driver.find_element(
            By.XPATH, '//div[@ng-if="$ctrl.section.hits.length > 0"]')

        # Find the first <a> tag inside the container and return its href
        top_result_link = container.find_element(
            By.CSS_SELECTOR, "a.mini_card").get_attribute('href')

        print(f"Top result obtained: {top_result_link}")
        return top_result_link

    except Exception as e:
        print("An error occurred:", e)
        return None

    finally:
        driver.quit()