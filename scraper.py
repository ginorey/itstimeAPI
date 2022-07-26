# Web Scraping
import requests as r
import json
from bs4 import BeautifulSoup as bs
# Data Manipulation
from collections import OrderedDict

i = open('links/links.json')
j = open('links/fighter_links.json')
directory = json.load(i)
fighter_links = json.load(j)


class scraper:
        # get fighter profile links
        def fighter_links():
            # initializing list
            temp = []

            # iterate through each site and pull all fighter links
            for link in directory:
                # try to connect to site
                try:
                    page = r.get(link,headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}, timeout=10)
                # if request fails, print URL and continue
                except r.exceptions.RequestException as i:
                    print(f'URL: {link}', i)
                    continue
                # read html
                s = bs(page.content, "html.parser")
                # locate all urls
                URLS = s.find_all('td', {'class': 'b-statistics__table-col'})

                # remove duplicate urls
                for link in URLS:
                    if(link.find('a')):
                        temp.append(link.find('a').get('href'))

            # convert to list
            links = list(OrderedDict.fromkeys(temp))
            # returns links list
            return links

        # gets all fighter info
        def fighters_info():
            # opening json file for links
            # getting and reading urls in links
            data = {"data" : []}
            id_counter = 1
            for url in fighter_links:

                # try to site html and read it
                try:
                    page = r.get(url, headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}, timeout=10)
                # if request fails, print URL and continue
                except r.exceptions.RequestException as i:
                    print(f'URL: {url}', i)    
                    continue
                # read html
                s = bs(page.content, "html.parser") 

                # find all fighter info
                NAME = s.find('span', {'class': 'b-content__title-highlight'})
                RECORD = (s.find('span', {'class': 'b-content__title-record'})).text.strip()
                NICKNAME = s.find('p', {'class': 'b-content__Nickname'})
                DESCRIPTION = s.find_all('li', {'class': 'b-list__box-list-item b-list__box-list-item_type_block'})

                # dictionary format
                format = {'ID': id_counter, 
                                  'name': '', 
                                'record': '', 
                              'nickname': '', 
                                'height': '',
                                'weight': '',
                                 'reach': '',
                                'stance': '',
                                  'dob' : '',
                                  'SLpM': '',
                              'Str. Acc': '',
                                  'SApM': '',
                              'Str. Def': '',
                              'TD Avg.' : '',
                              'TD Acc.' : '',
                               'TD Def' : '',
                            'Sub. Avg.' : '',
                }

                # remove all white spaces and format
                text_only = []
                for info in DESCRIPTION:
                    # append to RAW, text only
                    text_only.append(info.text.strip())
                temp = [key_val.split(":")[-1].strip() for key_val in text_only]

                # append each fighter info to format
                format['name']= NAME.text.strip()
                format['record'] = RECORD[8:]
                format['nickname'] = NICKNAME.text.strip()
                format['height'] = temp[0]
                format['weight'] = temp[1]
                format['reach'] = temp[2]
                format['stance'] = temp[3]
                format['dob'] = temp[4]
                format['SLpM'] = temp[5]
                format['Str. Acc'] = temp[6]
                format['SApM'] = temp[7]
                format['Str. Def'] = temp[9]
                format['TD Avg.'] = temp[10]
                format['TD Acc.'] = temp[11]
                format['TD Def'] = temp[12]
                format['Sub. Avg.'] = temp[13]

                # append dictionary to data
                data["data"].append(format)
                # add to id counter
                id_counter += 1

            # return data
            return data