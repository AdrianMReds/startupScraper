import os.path
from scraper import Scraper
from startup import Startup
import csv
import pandas

class FileWriter:

    file_exists = os.path.exists('startups.csv')

    def __init__(self, fn) -> None:
        self.fileName = fn

    def write(self, s:list):
        lst = []
        d = {}

        for i in s:
            d['Name'] = i.name
            d['Location'] = i.location
            d['Description'] = i.description
            d['Accelerator'] = i.accelerator
            d['Batch'] = i.batch
            d['Status'] = i.status
            d['Webpage'] = i.webpage
            lst.append(d)
            d = {}
        
        fields = ['Name', 'Location', 'Description', 'Accelerator', 'Batch', 'Status', 'Webpage']
        with open(self.fileName, 'w', encoding='utf-8', newline='') as startupFile:
            writer = csv.DictWriter(startupFile, fieldnames=fields)

            writer.writeheader()
            for item in lst:
                print(item)
                writer.writerow(item)
