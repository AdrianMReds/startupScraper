#Scraping some startups from YC
#By @AdrianMReds

from scraper import Scraper

if __name__ == '__main__':
    print("Welcome to the Startup Scraper")

    s = Scraper()
    s.scrapeYCFromFile()