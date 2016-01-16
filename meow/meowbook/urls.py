from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

import views

urlpatterns = [
    url(r'^$', views.NewsFeedView.as_view(), name='newsfeed'),
    url(r'^add-picture$', views.add_picture_view, name='add-picture'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^discover/$', views.discover, name='discover'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^search/(?P<cat_name>.+)/$', views.search, name='search'),
    url(r'^view_status/(?P<pk>.+)/$', views.StatusCommentView.as_view(), name='status'),
    url(r'^viewPhoto/(?P<pk>.+)/$', views.PhotoView.as_view(), name='status'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
