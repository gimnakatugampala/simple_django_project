
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf.urls import url

urlpatterns = [
    url(r'^$', include('posts.urls')),
    path('admin/', admin.site.urls),
    path('posts/', include('posts.urls')),
]
