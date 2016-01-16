from django.shortcuts import redirect, render
from django.views.generic import View
from django.views.generic.list import ListView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from forms import CatStatusForm, LoginForm
from models import CatPicture,CatProfile,CatStatus, UserProfile

class LayoutView(View):

    def get_context_data(self, request, **kwargs):
        form = self.SearchBarForm(request)
        catList = UserProfile.cats
        if request.user.is_authenticated():
            user = request.user.username()
        else:
            user = "Failed user get"

        context = super(LayoutView, self).get_context_data(**kwargs)
        context['cats'] = catList
        context['search_form'] = form
        return context

    def post(self, request, *args, **kwargs):
        form = self.SearchBarForm(request.POST)
        if form.is_valid():
            searchToken = form.cleaned_data['text']
        redirect('search', searchToken)


class NewsFeedView(ListView,LayoutView):
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
        return redirect('newsfeed')


def login_view(request):
    if request.method == 'GET':
        form = LoginForm()
        context = {
            'form': form,
        }
        return render(request, 'login.html', context)
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is None:
            context = {
                'form': form,
                'message': 'Wrong username or password!'
            }
            return render(request, 'login.html', context)
        else:
            login(request, user)
            return redirect('newsfeed')


def logout_view(request):
    logout(request)
    return redirect('login')




def search(request, cat_name):
    cats = CatProfile.objects.filter(name__contains=cat_name).all()

    if request.method == 'GET':
        context = {
            'cats': cats,
        }
        return render(request, 'search.html', context)


def cat_status(request, pk):
    status =  CatStatus.objects.get(pk=pk)

    if request.method == 'GET':
        context = {
            'status': status,
        }
        return render(request, 'view_status.html', context)

