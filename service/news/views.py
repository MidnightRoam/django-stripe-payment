from django.shortcuts import render
from django.views.generic import ListView

from .models import Article, Tag


class NewsPageListView(ListView):
    """News page with list of articles"""
    template_name = 'news/news_page.html'
    model = Article

    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        articles = Article.objects.all()
        tags = Tag.objects.all()
        context.update({
            'articles': articles,
            'tags': tags,
            'title': 'News'
        })
        return context
