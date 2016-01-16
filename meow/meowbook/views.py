from django.shortcuts import render

from django.views.generic.list import ListView
from meow.meowbook.models import CatPictures


class NewsFeedView(ListView):
    model = CatPictures
    template_name = 'NewsFeed.html'

    def get_context_data(self, **kwargs):
        context = super(NewsFeedView, self).get_context_data(**kwargs)
        return context
