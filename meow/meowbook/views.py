from django.shortcuts import redirect, render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth import authenticate, login, logout
from forms import CatStatusForm, LoginForm, StatusCommentForm
from models import CatPicture,CatProfile,CatStatus,StatusComment


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
        return redirect('newsfeed')


class StatusCommentView(DetailView):
    model = CatStatus
    form_class = StatusCommentForm
    template_name = 'view_status.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            comment_status_post = StatusComment(text=text, cat=request.user.aicitrebuieadaugatapisicacurenta)
            comment_status_post.save()
        return redirect('/')

    def get_context_data(self, **kwargs):
        context = super(StatusCommentView, self).get_context_data(**kwargs)
        context['form'] = self.form_class()
        return context


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


