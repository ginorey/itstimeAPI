# load json 
import json
# read url
from util.url_reader import url_reader
# Data Manipulation
from collections import OrderedDict

def getFighterProfileLinks():
    i = open('links/links.json')
    directory = json.load(i)
    # initializing list
    temp = []

    # iterate through each site and pull all fighter links
    # directory consist of list of all of the links for fighter names A-Z
    # we will use this loop to iterate through all of the links
    # this will give us the links for each fighter profile
    for link in directory:
        # try to connect to the link
        html = url_reader(link)
        if html == None:
            continue

        # locate all urls
        URLS = html.find_all('td', {'class': 'b-statistics__table-col'})

        # remove duplicate urls
        for link in URLS:
            if(link.find('a')):
                temp.append(link.find('a').get('href'))

    # convert to list
    links = list(OrderedDict.fromkeys(temp))
    # returns links list
    return links