from django.conf.urls import url

import views

urlpatterns = [
    url(r'^$', views.NewsFeedView.as_view(), name='newsfeed'),
    url(r'^search/(?P<pk>\d+)/$', views.Search.as_view(), name='search_cat'),
]