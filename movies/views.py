# movies/views.py
from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie # importing movie model

# Create your views here.
def index(request):
    all_movies = Movie.objects.all()
    return render(request, "movies/index.html",{'movies':all_movies})
