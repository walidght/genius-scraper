from genius_scraper import get_artist_url, extract_all_songs
from json_utils import write_to_json_file


artist_name = "kanye west"

artist_link = get_artist_url(artist_name)

songs_link = artist_link + "/songs"

all_songs = extract_all_songs(songs_link)

write_to_json_file(all_songs, f"./data/{artist_link.split('/')[-1]}.json")
