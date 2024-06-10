import json

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