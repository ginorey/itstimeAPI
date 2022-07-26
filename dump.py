import json
from scraper import scraper


# dumps all fighter links into fighter_links.son
def fighter_links_dump(links):
    with open('links/fighter_links.json', 'w', encoding='utf-8') as f:
        json.dump(scraper.fighter_links(), f, ensure_ascii=False, indent=4)

# dumps all fighter info into fighter_info.json
def fighter_info_dump(data):
    with open('data/fighter_info.json', 'w', encoding='utf-8') as f:
        json.dump(scraper.fighters_info(), f, ensure_ascii=False, indent=4)