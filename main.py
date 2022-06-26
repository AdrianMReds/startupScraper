#Scraping some startups from YC
#By @AdrianMReds

from scraper import Scraper
from fileWriter import FileWriter



if __name__ == '__main__':
    print("Welcome to the Startup Scraper")

    s = Scraper()
    fw = FileWriter('startups.csv')

    s.scrapeYCFromFile()
    s.scrapeFromWeb()
    
    # fw.write(s.startupList)

