from json_utils import write_to_json_file
from json_utils import get_all_songs


all_songs = get_all_songs(f"./data/kanye-west.json")


print(f"total songs: {len(all_songs)}")

# Filter songs to keep only songs that have kanye as main artist

kanye_songs = [
    (song["name"], song["link"]) for song in all_songs if "kanye-west" in song["link"].lower()]

print(f"total songs after processing: {len(kanye_songs)}")

# Save the filtered songs to a new JSON file

write_to_json_file(kanye_songs, f"./data/kanye-west-filtered.json")
