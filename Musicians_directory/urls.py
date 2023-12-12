 
from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home, name='homepage'),
    path('albums/', include('album.urls')),
    path('musicians/', include('musician.urls')),
]
