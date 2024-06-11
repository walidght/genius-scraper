import json
import random


def write_to_json_file(data_list, filename='data.json'):
    """
    Write a JSON file with a list of (name, link) tuples.

    Parameters:
    data_list (list of tuples): List of (name, link) tuples to write.
    filename (str): The name of the JSON file. Default is 'data.json'.
    """
    # Convert the list of tuples to a list of dictionaries
    data = [{"name": name, "link": link} for name, link in data_list]

    # Write the list to the JSON file, overwriting any existing content
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

    print(f"Data saved to {filename}")


def get_random_song(filename):
    """
    Get the title and URL of a random song from a JSON file.

    Parameters:
    filename (str): The name of the JSON file. Default is 'data.json'.

    Returns:
    tuple: A tuple containing the title and URL of a random song, or (None, None) if the file is empty or invalid.
    """
    try:
        # Read the data from the JSON file
        with open(filename, 'r') as json_file:
            data = json.load(json_file)

        # Check if the data is a list and has at least one item
        if isinstance(data, list) and data:
            # Select a random song from the list
            random_song = random.choice(data)
            # Ensure the item has 'name' and 'link' keys
            if 'name' in random_song and 'link' in random_song:
                return random_song['name'], random_song['link']

        # If data is empty or not as expected, return None
        return None, None

    except (json.JSONDecodeError, FileNotFoundError):
        # If there is an error in reading or parsing the file, return None
        return None, None


def get_all_songs(filename):
    try:
        # Read the data from the JSON file
        with open(filename, 'r') as json_file:
            data = json.load(json_file)

        # Check if the data is a list and has at least one item
        if isinstance(data, list) and data:
            return data

        # If data is empty or not as expected, return None
        return None

    except (json.JSONDecodeError, FileNotFoundError):
        # If there is an error in reading or parsing the file, return None
        return None
