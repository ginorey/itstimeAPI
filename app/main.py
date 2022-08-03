# pulls all fighter info and links
from scraper import scraper
# dumps all data into jsons
from dump import fighter_info_dump 
from dump import fighter_links_dump
# keeps track of runtime
import timeit


# Tracking wall runtime
start = timeit.default_timer()

# runs all functions and updates jsons 
def main():
    # update fighter links
    print('1/8 - Collecting Fighter Profile Links.')
    links = scraper.fighter_links()
    print("2/8 - Fighter Profile Links: DONE!")
    print("3/8 - Started to dump links in JSON.")
    fighter_links_dump(links)
    print("4/8 - Links dumped in JSON. DONE!")
    # update fighter info
    print('5/8 - Starting to pull fighter profile information.')
    info = scraper.fighters_info()
    print("6/8 - Fighter Profile Information.")
    print("7/8 - Started dumping info to JSON")
    fighter_info_dump(info)
    print("8/8 - DUMPED INFORMATION!")


main()
stop = timeit.default_timer()
print('Time: ', stop - start)
