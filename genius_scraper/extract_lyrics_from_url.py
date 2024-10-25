
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from genius_scraper.create_a_webdriver import create_a_webdriver
from .accept_cookies import accept_cookies


def extract_lyrics_from_url(url, driver=None):

    if driver is None:
        driver = create_a_webdriver()

        # Visit the song URL
        driver.get(url)

        # Accept cookies if prompted
        accept_cookies(driver)

    else:
        # Visit the song URL
        driver.get(url)

    song_data = dict()

    # Find the song title
    try:
        title_element = driver.find_element(
            By.CSS_SELECTOR, 'h1.SongHeaderdesktop__Title-sc-1effuo1-8')
        song_data['title'] = title_element.text
    except Exception as e:
        print('Song title could not be found')
        return None

    try:
        # Find all divs with the attribute data-lyrics-container="true"
        lyrics_containers = driver.find_elements(
            By.CSS_SELECTOR, 'div[data-lyrics-container="true"]')

        # Extract text from each container and join them
        song_data['lyrics'] = "\n".join(
            container.text for container in lyrics_containers)
    except Exception as e:
        print('Lyrics could not be found')
        return None

    try:
        # Extract release date
        release_date_element = driver.find_element(
            By.CSS_SELECTOR, 'div.MetadataStats__Container-sc-1t7d8ac-0 span.LabelWithIcon__Label-hjli77-1.hgsvkF')
        song_data['release_date'] = release_date_element.text
    except Exception as e:
        print('Release date could not be found')

    try:
        # Extract views
        views_element = driver.find_element(
            By.XPATH, '//span[contains(text(), "views")]/..')
        # Extract the number of views
        song_data['views'] = views_element.text.split()[0]
    except Exception as e:
        print('Views number could not be found')

    try:
        # Extract primary album
        album_element = driver.find_element(
            By.CSS_SELECTOR, 'a[href="#primary-album"].StyledLink-sc-3ea0mt-0.iegxRM')
        song_data['primary_album'] = album_element.text
    except Exception as e:
        print('Primary Album could not be found')

    # Click the "Read More" button if it exists
    try:
        read_more_button = driver.find_element(
            By.CSS_SELECTOR, 'span.HeaderBio__ViewBio-oaxemt-2.dggIzN')
        read_more_button.click()
        time.sleep(0.1)  # Wait for the content to expand
    except Exception as e:
        print(f"No 'Read More' button found or error occurred: {e}")

    # Click the "Read More" button if it exists
    try:
        # Find the element containing song description
        song_description_element = driver.find_element(
            By.CLASS_NAME, 'SongDescription__Content-sc-615rvk-2.kRzyD')
        song_data['song_description'] = song_description_element.text
    except Exception as e:
        print("Song description not found")

    # Click the "Expand" button
    try:
        expand_button = driver.find_element(
            By.CSS_SELECTOR, 'button.Button__Container-rtu9rw-0.ExpandableContent__Button-sc-1165iv-1')
        actions = ActionChains(driver)
        actions.move_to_element(expand_button).perform()
        time.sleep(0.1)  # Wait for the content to expand
        expand_button.click()
        time.sleep(0.1)  # Wait for the content to expand
    except Exception as e:
        print(f"No 'Expand' button found or error occurred: {e}")

    try:
        # Wait until the tags container is visible
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.SongTags__Container-xixwg3-1'))
        )

        # Then get the tag elements
        tag_elements = driver.find_elements(By.CSS_SELECTOR, 'div.SongTags__Container-xixwg3-1 a')
        
        # Extract the text from each tag element
        song_data['tags'] = [tag.text for tag in tag_elements if tag.text]

        if '' in song_data['tags']:
            raise Exception("Something wrong with tags")
    except Exception as e:
        print(e)

    return song_data
