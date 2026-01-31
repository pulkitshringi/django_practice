# movies/urls.py
from django.urls import path
from . import views # here . represents current directory

app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:movie_id>', views.detail, name='detail')
]