# pulls all fighter info and links
from src.scraper import getFighterProfileLinks, url_reader, fighterName, get_fighter_info
from src.scraper import fighterRecord, fighterNickname, fighterDescription, fightDetails, fighterObjectMaker, eventObjectMaker 
# dumps all data into jsons
from src.util.dump import dump
# keeps track of runtime
import timeit



# runs all functions and updates jsons 
def main():
    # Tracking wall runtime
    start = timeit.default_timer()

    # get fighter profile links
    print('1/8 - Collecting Fighter Profile Links.')
    links = getFighterProfileLinks() 
    print("2/8 - Fighter Profile Links: DONE!")

    # dump fighter profile links
    print("3/8 - Started to dump links in JSON.")
    dump.fighter_links(links)
    print("4/8 - Links dumped in JSON. DONE!")
    
    
    # get fighter info
    print('5/8 - Starting to pull fighter profile information.')
    data = get_fighter_info()
    print("6/8 - Fighter Profile Information: DONE!.")

    # dump fighter info
    print("7/8 - Started dumping info to JSON")
    dump.fighter_info(data)
    print("8/8 - DUMPED INFORMATION!")

    stop = timeit.default_timer()
    print('Runtime: ', stop - start)

main()
