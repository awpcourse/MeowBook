from django.conf.urls import url

import views

urlpatterns = [
    url(r'^$', views.NewsFeedView.as_view(), name='newsfeed'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
