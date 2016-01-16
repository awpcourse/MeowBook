from django.shortcuts import render

from django.views.generic.list import ListView
from models import CatPictures
from django.contrib.auth.decorators import login_required

class NewsFeedView(ListView):
    model = CatPictures
    template_name = 'NewsFeed.html'

    def get_context_data(self, **kwargs):
        context = super(NewsFeedView, self).get_context_data(**kwargs)
        context['form'] = self.form_class()
        return context



@login_required
def post_details(request, pk):
    cats = CatPictures.objects.get(name=pk)
    if request.method == 'GET':
        context = {
            'cats': cats,
        }
        return render(request, 'search.html/', context)
