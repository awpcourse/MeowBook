from django.shortcuts import redirect
from django.views.generic.list import ListView

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
