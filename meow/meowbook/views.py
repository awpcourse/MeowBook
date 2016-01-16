from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from forms import CatStatusForm
from models import CatPicture,CatProfile


class NewsFeedView(ListView):
    model = CatPicture
    form_class = CatStatusForm
    template_name = 'newsfeed.html'

    def get_context_data(self, **kwargs):
        context = super(NewsFeedView, self).get_context_data(**kwargs)
        context['form'] = self.form_class()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            user_post = CatStatusForm(text=text, author=request.user)
            user_post.save()
        return redirect('index')


def search(request, cat_name):
    cats = CatProfile.objects.filter(name__contains=cat_name).all()

    if request.method == 'GET':
        context = {
            'cats': cats,
        }
        return render(request, 'search.html', context)
