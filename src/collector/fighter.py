
# returns fighterName string
def fighterName(html):
    name = html.find('span', {'class': 'b-content__title-highlight'}).text.strip()
    return name

# returns fighterRecord string
def fighterRecord(html):
    record = (html.find('span', {'class': 'b-content__title-record'})).text.strip()
    return record

# returns fighterNickname string
def fighterNickname(html):
    nickname = html.find('p', {'class': 'b-content__Nickname'}).text.strip()
    return nickname

# returns fighterName string
def fighterDescription(html):
    # removing all whitespaces in the raw html
    # then append to text_only
    # text_only is a list of all fighter information
    temp = html.find_all('li', {'class': 'b-list__box-list-item b-list__box-list-item_type_block'})
    text_only = []
    for info in temp:
        # append to text only
        text_only.append(info.text.strip())
        # thanks to stack over flow
    description = [key_val.split(":")[-1].strip() for key_val in text_only]
    return description