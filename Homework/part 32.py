import csv

import requests
from bs4 import BeautifulSoup


def get_html(url):
    res = requests.get(url)
    return res.text


def get_data(html):
    soup = BeautifulSoup(html, "lxml")
    p1 = soup.find_all("div", class_="wallpapers__item")
    data = [['Информация о фото', 'Ссылка на фото', 'Размер фото']]
    for i in p1:
        temp = []
        info = i.find("a")["title"]
        photo = i.find("img")["src"]
        size = i.find("small").text
        temp.append(info)
        temp.append(photo)
        temp.append(size)
        data.append(temp)
    write_csv(data)


def write_csv(lst):
    with open('pictures.csv', 'w') as f:
        writer = csv.writer(f, delimiter=';', lineterminator='\r')
        writer.writerows(lst)


def main():
    url = "https://www.goodfon.ru/"
    get_data(get_html(url))


if __name__ == '__main__':
    main()