
from urllib.request import urlopen
from bs4 import BeautifulSoup


def get_ranobe(href):

    html = urlopen(href)
    info=''
    bsObj = BeautifulSoup(html.read(), 'lxml')
    for sibling in bsObj.findAll("div", class_="item__point-list-content"):
        info = sibling.find('ul')
        check = info.find('li').get_text()
        info = check[2:-6]
    return info

