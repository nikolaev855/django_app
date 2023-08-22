from django.contrib import admin
from django.conf.urls import include
from django.conf.urls.static import static
from django.urls import re_path
from feed import urls as feed_urls
from django.conf import settings

urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path("", include(feed_urls, namespace="feed")),
    re_path("", include("allauth.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  