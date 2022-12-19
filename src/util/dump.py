import json
from models.encoder import FighterJSONENCODER

class dump:
    # dumps all fighter links into fighter_links.son
    def fighter_links(links):
        with open('links/fighter_links.json', 'w', encoding='utf-8') as f:
            json.dump(links, f, default = str, ensure_ascii=False, indent=4)

    # dumps all fighter info into fighter_info.json
    def fighter_info(fighter):
        with open('src/data/data.json', 'w', encoding='utf-8') as f:
            json.dump(fighter, f, cls=FighterJSONENCODER,ensure_ascii=False, indent=4)