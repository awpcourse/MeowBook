from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

import views

urlpatterns = [
    url(r'^$', views.NewsFeedView.as_view(), name='newsfeed'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
