
from urllib.request import urlopen
from bs4 import BeautifulSoup


def get_webtoon(href):

    html = urlopen(href)
    info = ''
    bsObj = BeautifulSoup(html.read(), 'lxml')
    for sibling in bsObj.findAll("div", class_="detail_lst"):
        info = sibling.find('ul').find('li').find('span', class_='date')
    return info.get_text().strip()
