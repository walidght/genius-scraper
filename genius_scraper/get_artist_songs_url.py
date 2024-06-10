from genius_scraper import get_artist_url

def get_artist_songs_url(artist_name):
    artist_link = get_artist_url(artist_name)

    return artist_link + "/songs"