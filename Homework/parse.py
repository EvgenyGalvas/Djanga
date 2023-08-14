import csv

import requests
from bs4 import BeautifulSoup


class Parser:

    html = ''
    res = []

    def __init__(self, url, file):
        self.url = url
        self.file = file

    def get_html(self):
        req = requests.get(self.url).text
        self.html = BeautifulSoup(req, 'lxml')

    def parsing(self):
        news = self.html.find_all('li', class_='content-list__item')
        for item in news:
            title = item.find('div', class_='task__title').get('title')
            price = item.find('div', class_='task__price').find_all('span')[1].text
            data = {
                'title': title,
                'price': price
            }
            self.res.append(data)

    def write_csv(self):
        with open(self.file, 'w', encoding='utf-8-sig') as f:
            write = csv.writer(f, delimiter=';', lineterminator='\r')

            for k in self.res:
                write.writerow(k.values())

    def run(self):
        self.get_html()
        self.parsing()
        self.write_csv()