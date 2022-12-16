# Web Scraping
import requests as r
import json
# read html
from util import url_reader
from models.models import Fighter
from models.models import Event
from collector.fighter import fighterName, fighterDescription, fighterNickname, fighterRecord
from collector.events import fightDetails
from objects import eventObjectMaker, fighterObjectMaker
    
def get_fighter_info():
    # pull up fighter profile links 
    j = open('links/fighter_links.json')
    fighter_links = json.load(j)

    data = {"data" : []} 
    id_counter = 1

    # iterate over fighter profile links
    for link in fighter_links:

        # collect and read html
        html = url_reader(link)
        if html == None:
            continue
        
        # collect data
        name         = fighterName(html)
        record       = fighterRecord(html)
        nickname     = fighterNickname(html)
        description  = fighterDescription(html)
        fightDetail  = fightDetails(html)

        # make objects
        fights = eventObjectMaker(fightDetail)
        fighter = fighterObjectMaker(id_counter, name, record, nickname, description, fights)
        data['data'].append(fighter)
        id_counter += 1
    
    return data 