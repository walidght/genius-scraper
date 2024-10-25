from genius_scraper import get_artist_songs_url, extract_all_songs, fetch_lyrics_for_all_songs, write_to_json_file
import sys

if __name__ == "__main__":
    artist_name = arg1 = sys.argv[1]

    songs_link = get_artist_songs_url(artist_name)

    all_songs = extract_all_songs(songs_link)

    songs_file_path = f"./data/v3/{songs_link.split('/')[-2]}.json"

    write_to_json_file(all_songs, songs_file_path)

    fetch_lyrics_for_all_songs(songs_file_path)