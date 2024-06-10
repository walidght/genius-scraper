# Genius Scraper

Genius Scraper is a Python package for scraping song data from the Genius website. It provides functions to extract song information for a given artist and save the data in JSON format.

## Features

-   Fetch artist URLs based on search queries.
-   Extract song information, including titles and URLs, from artist pages.
-   Save song data to JSON files for further analysis.

## Installation

1. Clone the repository:

```
git clone https://github.com/walidght/genius-scraper.git
```

2. Install dependencies:

```
pip install -r requirements.txt
```

## Usage

1. Import the `genius_scrapper` package:

```python
from genius_scrapper import get_artist_url, extract_all_songs
```

2. Use the provided functions to fetch artist URLs and extract song data:

```python
# Example usage: Fetch artist URL
artist_url = get_artist_url('Immortal Technique')

# Example usage: Extract all songs
songs_data = extract_all_songs(artist_url)
```

3. View the extracted data in JSON format:

```python
import json
print(json.dumps(songs_data, indent=4))
```

## Configuration

The package configuration is stored in a JSON file named `configs.json`. You can customize the Chrome options and Chromedriver path in this file.

Example `configs.json`:

```json
{
    "chrome_options": {
        "headless": true,
        "disable-gpu": true
    },
    "chromedriver_path": "/path/to/chromedriver"
}
```
