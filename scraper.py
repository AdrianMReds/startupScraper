from tracemalloc import start
from bs4 import BeautifulSoup

from startup import Startup
import requests

class Scraper:

    startupList = []

    def __init__(self, url=''):
        self.url = url

    def printList(self, lst, rng) -> None:
        for x in range(rng):
            print(lst[x])


    def scrapeYCFromFile(self):

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
                st = st.replace(' ', '.')
                st = st.replace('.....................', '.')
                st = st.replace('.................', '.')
                st = st.replace('..', '.')
                st = st.replace('...', '.')
                st = st.replace('|', '')
                st = st.replace('...', '$$')
                slist.append(st)

            startups = []

            for i in slist:
                startups.append(i.split('$$'))

            topop = []
            for s in startups:
                for i in range(len(s)):
                    if s[i] == '' or s[i] == '.':
                        topop.append(i)
                    else:
                        s[i] = s[i].strip('.')
                topop.reverse()
                for t in topop:
                    s.pop(t)
                topop.clear()

                print(s[0], s[2], s[1], 'Y Combinator')

                so = Startup(s[0], s[2], s[1], 'Y Combinator')

            print(len(startups))