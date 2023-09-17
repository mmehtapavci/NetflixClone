from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('movies/<profilId>/<slug:slug>', movies, name='movies'),
    path('video/<movieId>/', video, name='video')
]