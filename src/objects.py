from models.fight import Fight
from models.fighter import Fighter

def fighterObjectMaker(id_counter, name, record, nickname, description, fights):
    fighter = Fighter(id_counter, name, record[8:], nickname, description[0], description[1], description[2], description[3], description[4],
                    description[5], description[6], description[7], description[9], description[10], description[11], description[12], description[13], fights)
    return fighter 

def eventObjectMaker(fightDetails):
    fights = []
    fight_counter = 1
    for fight in fightDetails:
        # make fight object
        fight = Fight(fight_counter, fight[0], fight[1], fight[2], fight[3], fight[4], fight[5], fight[6],
                      fight[7], fight[8], fight[9], fight[10], fight[11], fight[12], fight[13], fight[14], fight[15])
        # append to fights list
        fights.append(fight)
        # increase counter by 1 
        fight_counter += 1
    return fights