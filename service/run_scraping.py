import codecs
import os
import sys
import django
from django.db import DatabaseError


proj = os.path.dirname(os.path.abspath('manage.py'))
sys.path.append(proj)
os.environ['DJANGO_SETTINGS_MODULE'] = 'service.settings'

django.setup()

from news.scraping import stopgame_news_scrap
from news.models import Article, Tag

parsers = (
    (stopgame_news_scrap, 'https://stopgame.ru/news'),
)

article = Article.objects.all()
news, errors = [], []
for func, url in parsers:
    n, e = func(url)
    news += n
    errors += e

for article_dict in news:
    a = Article()
    a.url = article_dict['url']
    a.title = article_dict['title']
    a.image = article_dict['image']
    try:
        a.save()
    except DatabaseError:
        pass

h = codecs.open('news.json', 'w', encoding='utf-8')
h.write(str(news))
h.close()
