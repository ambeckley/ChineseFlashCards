import requests
from bs4 import BeautifulSoup
import json

# Dictionary to hold flashcards based on HSK level
flashcards = {
    'HSK1': [],
    'HSK2': [],
    'HSK3': [],
    'HSK4': [],
    'HSK5': [],
    'HSK6': [],
}

def scrape_hsk_words(level):
    level_number = level.split('HSK')[-1]  # Extract the level number
    url = f"https://hsk.academy/en/hsk-{level_number}-vocabulary-list"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to retrieve {url}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the vocabulary table
    words_table = soup.find('table')
    if words_table:
        rows = words_table.find_all('tr')[1:]  # Skip the header row
        for row in rows:
            columns = row.find_all('td')
            if len(columns) >= 2:
                chinese = columns[0].text.strip()
                english = columns[1].text.strip()
                flashcards[level].append({"chinese": chinese, "english": english})

# Scrape all HSK levels
for level in flashcards.keys():
    scrape_hsk_words(level)

# Save to a JSON file
with open('hsk_flashcards.json', 'w', encoding='utf-8') as f:
    json.dump(flashcards, f, ensure_ascii=False, indent=4)

print("HSK vocabulary has been saved to hsk_flashcards.json.")
