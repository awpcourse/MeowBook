from django.contrib.auth import authenticate, login, logout
from django.core.files.uploadedfile import SimpleUploadedFile
from django.shortcuts import redirect, render
from django.views.generic import View
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from forms import CatStatusForm, LoginForm, AddPicForm
from forms import StatusCommentForm, PhotoCommentForm
from models import CatPicture,CatProfile,CatStatus, UserProfile
from models import StatusComment,PictureComment
import urlparse

class LayoutView(View):


    def post(self, request, *args, **kwargs):
        form = self.SearchBarForm(request.POST)
        if form.is_valid():
            searchToken = form.cleaned_data['text']
        redirect('search', searchToken)


class NewsFeedView(ListView, LayoutView):
    model = CatPicture
    form_class = CatStatusForm
    template_name = 'newsfeed.html'
    current_cat = None

    def get_context_data(self, **kwargs):
        self.current_cat = self.request.GET.get('current_cat')
        context = super(NewsFeedView, self).get_context_data(**kwargs)
        # import pdb;pdb.set_trace()
        context['form'] = self.form_class()
        context['current'] = self.current_cat
        return context

    def post(self, request, *args, **kwargs):
        # current_cat = self.request.GET.get('current_cat')
        form = self.form_class(request.POST)
        # import pdb;pdb.set_trace()
        if form.is_valid():
            text = form.cleaned_data['text']
            user_post = CatStatus(text=text, cat=CatProfile.objects.get(pk=self.current_cat))
            user_post.save()
        return redirect('newsfeed')


def add_picture_view(request):
    if request.method == 'GET':
        form = AddPicForm()
        return render(request, 'add-picture.html', {'form': form})
    elif request.method == 'POST':
        import pdb;pdb.set_trace()
        form = AddPicForm(request.POST, request.FILES)
        if form.is_valid():
            pic = request.FILES['pic']
            desc = form.cleaned_data['desc']
            cat_pic = CatPicture(picture=pic, description=desc, cat=CatProfile.filter(pk=request.get('current_cat_pk')))
            cat_pic.save()
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


class PhotoView(DetailView):
    model = CatPicture
    form_class = PhotoCommentForm
    template_name = 'viewPhoto.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            picture_comment = PictureComment(text=text)
            picture_comment.save()
        return redirect('/')

    def get_context_data(self, **kwargs):
        context = super(PhotoView, self).get_context_data(**kwargs)
        context['form'] = self.form_class()
        return context


class ProfileView(DetailView):
    model = CatProfile
    template_name = 'viewProfile.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        # context['form'] = self.form_class()
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


def cat_status(request, pk):
    status = CatStatus.objects.get(pk=pk)

    if request.method == 'GET':
        context = {
            'status': status,
        }
        return render(request, 'view_status.html', context)


def discover(request):
    if request.method == 'GET':
        pictures = CatPicture.objects.all()
        context = {
            'pictures': pictures,
        }
        return render(request, 'discover.html', context)
