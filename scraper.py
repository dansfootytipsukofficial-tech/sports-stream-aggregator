import requests
import json
from datetime import datetime
import time
import random
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

STREAM_SITES = [
    "https://sportsurge.net",
    "https://crackstreams.is",
    "https://streameast.live",
    "https://buffstreams.tv",
    "https://ustvgo.tv",
    "https://freeintertv.com",
    "https://streamlive.to",
    "https://tv247.us",
    "https://lookmovie2.to",
    "https://fmovies.to",
    "https://soap2day.ac",
    "https://putlocker.pe"
]

def scrape_stream_sites():
    streams = []
    for site in STREAM_SITES:
        try:
            print(f"Scraping {site}...")
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
            response = requests.get(site, headers=headers, timeout=10, verify=False)
            if response.status_code == 200:
                streams.append({
                    'site': site,
                    'title': f"Live streams from {site}",
                    'link': site,
                    'timestamp': datetime.now().isoformat()
                })
                time.sleep(random.uniform(1, 3))
            else:
                print(f"Failed to fetch {site}: {response.status_code}")
        except Exception as e:
            print(f"Error scraping {site}: {e}")
    return streams

def scrape_reddit():
    print("Scraping Reddit...")
    return [
        {
            'site': 'Reddit',
            'title': 'Reddit soccer streams',
            'link': 'https://reddit.com/r/soccerstreams',
            'timestamp': datetime.now().isoformat()
        }
    ]

def scrape_sportmonks():
    print("Fetching SportMonks data...")
    return [
        {
            'site': 'SportMonks',
            'title': 'Premier League fixtures',
            'link': 'https://api.sportmonks.com/v3/football/fixtures',
            'timestamp': datetime.now().isoformat()
        }
    ]

def main():
    print("Starting stream aggregation...")
    
    all_streams = []
    all_streams.extend(scrape_stream_sites())
    all_streams.extend(scrape_reddit())
    all_streams.extend(scrape_sportmonks())
    
    with open('streams.json', 'w') as f:
        json.dump(all_streams, f, indent=2)
    
    print(f"Saved {len(all_streams)} streams to streams.json")

if __name__ == "__main__":
    main()
