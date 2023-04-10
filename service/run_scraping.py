import codecs
import os
import sys
import django
from django.db import DatabaseError

from news.scraping import stopgame_news_scrap
from news.models import Article, Tag, Error

proj = os.path.dirname(os.path.abspath('manage.py'))
sys.path.append(proj)
os.environ['DJANGO_SETTINGS_MODULE'] = 'service.settings'

django.setup()

parsers = (
    (stopgame_news_scrap, 'https://stopgame.ru/news'),
)

article = Article.objects.all()
tags = Tag.objects.all()
news, errors = [], []
# loop = asyncio.get_event_loop()
# tmp_task = [(func, article_dict.get(url), article_dict['url'], article_dict['title'], article_dict['image'])
#             for func, url in parsers
#             for article_dict in news]
# tasks = asyncio.wait([loop.create_task(main(f)) for f in tmp_task])
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
if errors:
    error = Error(data=errors).save()

h = codecs.open('news.json', 'w', encoding='utf-8')
h.write(str(news))
h.close()
