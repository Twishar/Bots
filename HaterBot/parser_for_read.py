import json

from urllib.request import urlopen
from bs4 import BeautifulSoup


def get_read_mang(href):

    html = urlopen(href)
    info = ''
    bsObj = BeautifulSoup(html.read(), 'lxml')
    for sibling in bsObj.findAll("table", class_="table table-hover"):
        info = sibling.find('td', class_='hidden-xxs').get_text().strip()
    return info


