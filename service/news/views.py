from django.shortcuts import render
from django.views.generic import ListView

from .models import Article, Tag


class NewsPageListView(ListView):
    """News page with list of articles"""
    template_name = 'news/news_page.html'
    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get('slug')
        if slug:
            tag = Tag.objects.get(slug=slug)
            articles = Article.objects.filter(tags__pk=tag.pk).order_by('-id')
        else:
            articles = Article.objects.all().order_by('-id')
        tags = Tag.objects.all()
        context.update({
            'articles': articles,
            'tags': tags,
            'title': 'News'
        })
        return context


