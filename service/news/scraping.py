import requests
import codecs
from bs4 import BeautifulSoup as BS
from random import randint

__all__ = ("stopgame_news_scrap", )

headers = [
    {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0',
     'Accept': 'text/html, application/xhtml+xml, application/xml:q=0.9,*/*;q=0.8'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:51.0) Gecko/20100101 Firefox/51.0',
     'Accept': 'text/html, application/xhtml+xml, application/xml:q=0.9,*/*;q=0.8'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:53.0) Gecko/20100101 Firefox/53.0',
     'Accept': 'text/html, application/xhtml+xml, application/xml:q=0.9,*/*;q=0.8'},
]


def stopgame_news_scrap(url):
    news = []
    errors = []
    domain = 'https://stopgame.ru'
    url = 'https://stopgame.ru/news'
    response = requests.get(url, headers=headers[randint(0, 2)])
    if response.status_code == 200:
        soup = BS(response.content, 'html.parser')
        main_div = soup.find('div', attrs={"class": 'items'})
        if main_div:
            div_lst = main_div.find_all('div', attrs={"class": "item"})
            for div in div_lst:
                title = div.find('div', attrs={"class": "caption"})
                href = title.a['href']
                image = div.find('img')['src']
                news.append({'title': title.text, 'url': domain + href, 'image': image})
        else:
            errors.append({'url': url, 'title': "Div doesn't exist"})
    else:
        errors.append({'url': url, 'title': "Page don't response"})

    return news, errors


if __name__ == '__main__':
    url = 'https://stopgame.ru/news'
    news, errors = stopgame_news_scrap(url)
    h = codecs.open('news.json', 'w', encoding='utf-8')
    h.write(str(news))
    h.close()
