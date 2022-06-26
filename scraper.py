from bs4 import BeautifulSoup
import requests

from startup import Startup

def wordsLeft(p:str) -> bool:
    for l in p:
        if l!='$' and l!='.':
            return True
    return False

def lookWords(p:str) -> list:
    # print('The string is {}'.format(p))
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-\''
    lst = []
    data = p
    counter = 0
    first = -1
    last = -1
    still = True

    while still:
        # print(len(data))
        # print('p by now is {}'.format(data))
        for i in range(len(data)):
            # if data[i]!='$' and data[i]!='.':
            if data[i] in alphabet:
                if first == -1:
                    # print('first is {}'.format(data[i]))
                    first = i
                    continue
            if data[i]=='$' and first!=-1:
                last = i
                break
        word = data[first:last]
        # print('Piece is {}'.format(word))
        lst.append(data[first:last])
        data = data[last+1:]
        first = -1
        last = -1
        still = wordsLeft(data)
    
    return lst

def lotsOfSpaces(s:str) -> str:
    counter = 0
    lots = False
    for i in range(len(s)):
        if lots and s[i]==' ':
            counter+=1
            continue
        if i != len(s)-1:
            if s[i]==' ' and s[i+1]==' ':
                lots = True
                counter += 1

    spaces = ' '*counter
    desc = s.replace(spaces, ' ')
    return desc

class Scraper:

    startupList = []

    def __init__(self, url=''):
        self.url = url

    def printList(self, lst, rng) -> None:
        for x in range(rng):
            print('{} {}'.format(x, lst[x]))

    #For this function I had to extract come of the code of ycombinator.com/companies manually
    def scrapeYCFromFile(self):
        with open('batches.html', encoding='utf-8') as page:
            soup = BeautifulSoup(page, 'html.parser')

            sdivs = soup.select('.right')
            info = []

            for s in sdivs:
                sinfo = s.get_text('$')
                info.append(sinfo)
            
            counter = 0
            slist = []
            for i in info:
                st = i.replace('\n', '')
                slist.append(st)
                counter+=1

            startups = []

            for i in slist:
                toadd = lookWords(i)
                for x in range(len(toadd)):
                    if x != 2:
                        toadd[x] = toadd[x].replace(' ', '')
                    else:
                        toadd[x] = toadd[x].replace('      ', '')
                        toadd[x] = toadd[x].replace('  ', ' ')
                startups.append(toadd)

            for s in startups:
                so = Startup(s[0], s[1], s[2], 'Y Combinator')
                so.batch = s[3]
                if len(s) > 4:
                    so.tags = s[4:]
                self.startupList.append(so)
    
    def scrapeFromWeb(self):
        webpage = requests.get('https://yclist.com/')
        soup = BeautifulSoup(webpage.content, 'html.parser')

        strs = soup.find_all('tr')
        info = []

        for s in strs:
            sinfo = s.get_text('$')
            info.append(sinfo)

        counter = 0
        slist = []
        for i in info:
            st = i.replace('\n', '')
            slist.append(st)
            counter+=1

        startups = []

        for i in slist:
            toadd = lookWords(i)
            if len(toadd) < 4:
                # print(toadd[0])
                if toadd[1].find('http') == -1:
                    toadd.insert(1, 'Unknown')
                else:
                    toadd.append('Unknown description')
            if toadd[1].find('http') == -1:
                toadd.insert(1, 'Unknown')
            if toadd[3] != 'exited' and toadd[3] != 'dead':
                toadd.insert(3, 'operating')
            if toadd[0] == 'AudioBeta':
                toadd[1] = 'Unknown'
                toadd[2] = 'W06'
                toadd[3] = 'operating'
                toadd[4] = 'Unknown description'
            
            for x in range(len(toadd)):
                if x != 4:
                    toadd[x] = toadd[x].replace(' ', '')
                else:
                    toadd[x] = toadd[x].strip()
            # print(toadd)
            startups.append(toadd)

        for s in startups:
            so = Startup(s[0], 'Unknown', '', 'Y Combinator')
            so.batch = s[2]
            if len(s) > 5:
                so.description = s[-1]
            else:
                so.description = s[4]
            so.status = s[3]
            print(so)
            self.startupList.append(so)

        
        # self.printList(startups, 1000)