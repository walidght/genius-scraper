from genius_scraper import accept_cookies, create_a_webdriver, extract_lyrics_from_url
from genius_scraper.json_utils import write_to_json_file
from genius_scraper.json_utils import get_all_songs
from genius_scraper.string_utils import clean_title
import os


def save_to_text_file(file_path, content):
    try:
        # Extract directory path
        directory = os.path.dirname(file_path)
        # Create directories if they don't exist
        os.makedirs(directory, exist_ok=True)

        with open(file_path, 'w') as file:
            file.write(content)
    except Exception as e:
        print(f"Error occurred while saving content to {file_path}: {str(e)}")


def fetch_lyrics_for_all_songs(songs_path):

    all_songs = get_all_songs(songs_path)

    total_songs_count = len(all_songs)
    print(f"total songs: {total_songs_count}")

    fails = []

    driver = create_a_webdriver()

    accept_cookies(driver)
    print()

    songs_data = []

    for i, song in enumerate(all_songs):
        name, link = song["name"], song["link"]
        file_name = clean_title("-".join(name.split(" ")))
        print(f"{i}/{total_songs_count} => fetching: {name}", end="\r")

        song_data = extract_lyrics_from_url(link, driver)

        if song_data:
            song_data['id'] = f"{i}"
            write_to_json_file(song_data, songs_path.replace(
                ".json", f"/{file_name}.json"))

            # songs_data.append(song_data)
        else:
            fails.append({"name": name, "link": link})
            print(fails[-1])

    if len(fails) > 0:
        write_to_json_file(fails, songs_path.replace(".json", "-failed.json"))
        print(
            f"failed to fetch {len(fails)} songs. Check failed.json for details.")

    driver.quit()

# title, link = get_random_song(f"./data/kanye_west.json")


# print(f"{title}\n\n{lyrics}")
