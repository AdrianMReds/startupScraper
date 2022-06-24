# from lib2to3.pgen2 import driver
# from optparse import Option
# import time
from logging.config import stopListening
from traceback import print_list
from tracemalloc import start
from bs4 import BeautifulSoup

from startup import Startup
import requests
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options

class Scraper:

    startupList = []

    def __init__(self, url=''):
        self.url = url

    def printList(self, lst, rng) -> None:
        for x in range(rng):
            print(lst[x])


    def scrapeYC(self):
        self.url = 'https://yclist.com/'

        with open('batches.html', encoding='utf-8') as page:
            soup = BeautifulSoup(page, 'html.parser')

            # print(soup.prettify())
            sdivs = soup.select('.right')
            info = []

            for s in sdivs:
                sinfo = s.get_text(' | ')
                info.append(sinfo)
            
            slist = []

            for i in info:
                st = i.replace('\n', '')
                st = st.replace(' ', '')
                st = st.replace('|', ' ')
                st = st.replace('  ', '.')
                st = st.replace('....', ' ')
                st = st.replace('..', ' ')
                st = st.replace('.', ' ')
                slist.append(st.strip(' '))

            startups = []

            for i in slist:
                startups.append(i.split())

            self.printList(startups, 10)

            # print(len(startups))