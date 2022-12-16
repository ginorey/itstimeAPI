import json

def fightDetails(html):
    fight_details = html.find_all('p', {'class': 'b-fight-details__table-text'})
    fight_details_text = []
    k = open('extra/forbbiden.json')
    forbidden = json.load(k)
    for i in fight_details:
        fight_details_text.append(i.text.strip())
    for i in fight_details_text:
        if i in forbidden:
            fight_details_text.remove(i)
        if i == 'next':
            pointer = fight_details_text.index(i)
            del fight_details_text[pointer:pointer+6]
                
    # Credit to StackOverflow for this Line
    fightDetails = [fight_details_text[i: i+16] for i in range(0, len(fight_details_text), 16)]
    return fightDetails