# movies/urls.py
from django.urls import path
from . import views # here . represents current directory

urlpatterns = [
    path('', views.index)
]