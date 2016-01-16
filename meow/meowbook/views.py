from django.shortcuts import render

from django.views.generic.list import ListView
from models import CatPicture


class NewsFeedView(ListView):
    model = CatPicture
    template_name = 'NewsFeed.html'

    def get_context_data(self, **kwargs):
        context = super(NewsFeedView, self).get_context_data(**kwargs)
        return context
