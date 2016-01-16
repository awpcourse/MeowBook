from django.conf.urls import url

import views

urlpatterns = [
    url(r'^$', views.NewsFeedView.as_view(), name='newsfeed'),
]