from tracemalloc import start
from bs4 import BeautifulSoup

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



class Scraper:

    print(lookWords('$GoSats$Bengaluru,.Karnataka,.India.$.GoSats.helps.you.earn.free.bitcoin.when.you.shop.in$$.India$$$$$.W22$DeFi$Crypto./.Web3$Fintech$Payments$E-commerce$'))

    startupList = []

    def __init__(self, url=''):
        self.url = url

    def printList(self, lst, rng) -> None:
        for x in range(rng):
            print('{} {}'.format(x, lst[x]))


    def scrapeYCFromFile(self):

        with open('batches.html', encoding='utf-8') as page:
            soup = BeautifulSoup(page, 'html.parser')

            # print(soup.prettify())
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
                    toadd[x] = toadd[x].replace(' ', '')
                startups.append(toadd)

            for s in startups:
                so = Startup(s[0], s[1], s[2], 'Y Combinator')
                so.batch = s[3]
                if len(s) > 4:
                    so.tags = s[4:]
                print(so)

                
                
            # self.printList(startups, 2214)
            #Podriamos cambiar el replace de \n para diferenciar en donde está cada sección de la startup
            print(len(startups))