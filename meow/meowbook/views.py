from django.shortcuts import redirect, render
from django.views.generic.list import ListView, View
from models import UserProfile, CatPictures

from forms import CatStatusForm
from models import CatPicture


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


class LayoutView(View):

    def get_context_data(self, request, **kwargs):
        catList = UserProfile.cats
        if request.user.is_authenticated():
            user = request.user.username()
        else:
            user = "Failed user get"

        context  = super(LayoutView, self).get_context_data(**kwargs)
        context ['cats'] = catList
        context ['loggedInUser'] = user

        return context

    def post(self, request, *args, **kwargs):
        form = self.SearchBarForm(request.POST)
        if form.is_valid():
            searchToken = form.cleaned_data['text']
        redirect('search', searchToken)
