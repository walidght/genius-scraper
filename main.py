from genius_scraper import get_artist_songs_url, extract_all_songs
from json_utils import write_to_json_file


artist_name = "kanye west"

songs_link = get_artist_songs_url(artist_name)

all_songs = extract_all_songs(songs_link)

write_to_json_file(all_songs, f"./data/{songs_link.split('/')[-2]}.json")
