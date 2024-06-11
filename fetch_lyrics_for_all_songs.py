from genius_scraper import create_a_webdriver, extract_lyrics_from_url
from json_utils import write_to_json_file
from json_utils import get_all_songs
from string_utils import clean_title
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


artist = "Kanye-west"

all_songs = get_all_songs(f"./data/{artist}-filtered.json")

total_songs_count = len(all_songs)
print(f"total songs: {total_songs_count}")

fails = []

driver = create_a_webdriver()
print()

for i, song in enumerate(all_songs):
    name, link = song["name"], song["link"]
    file_name = clean_title("-".join(name.split(" ")))
    print(f"{i}/{total_songs_count} => fetching: {name}", end="\r")

    lyrics = extract_lyrics_from_url(link, driver)
    if lyrics:
        save_to_text_file(f"./data/lyrics/{artist}/{file_name}.txt", lyrics)
    else:
        fails.append((name, link))

if len(fails) > 0:
    write_to_json_file(fails, f"./data/lyrics/{artist}/failed.json")
    print(
        f"failed to fetch {len(fails)} songs. Check failed.json for details.")

driver.quit()

# title, link = get_random_song(f"./data/kanye_west.json")


# print(f"{title}\n\n{lyrics}")
