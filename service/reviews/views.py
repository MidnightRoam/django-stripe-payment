from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView

from products.models import Item
from .models import ItemRating
from .forms import ItemRatingForm


class ItemRatingDetailView(DetailView):
    """Item rating detail view"""
    template_name = 'reviews/reviews_form.html'
    login_url = reverse_lazy('login')

    def get(self, *args, **kwargs):
        current_item = Item.objects.get(slug=self.kwargs['slug'])
        context = {
            'item': current_item,
            'title': f'{current_item} Reviews',
        }
        return render(self.request, self.template_name, context)


class AddReviewView(LoginRequiredMixin, View):
    """Add review view"""
    def post(self, request, pk, *args, **kwargs):
        form = ItemRatingForm(request.POST)
        item = get_object_or_404(Item, pk=pk)
        if form.is_valid():
            # Проверяем, делал ли пользователь ранее отзыв на этот продукт
            if ItemRating\
                    .objects\
                    .filter(user=self.request.user)\
                    .filter(item_id=item)\
                    .exists():
                return redirect('reviews', slug=item.slug)  # Если да, то редирект
                # на страницу с обзорами этого продукта
            # Save form data to the database
            rating = form.save(commit=False)
            rating.item = item
            rating.user = request.user
            rating.rate = form.cleaned_data['rate']
            rating.text = form.cleaned_data['text']
            rating.save()
            return redirect('reviews', slug=item.slug)
        else:
            return redirect('index')

