# movies/views.py
from django.shortcuts import render, get_object_or_404 # import shortcut first
from django.http import HttpResponse
from .models import Movie 

# Create your views here.
def index(request):
    all_movies = Movie.objects.all()
    return render(request, "movies/index.html",{'movies': all_movies})

def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, "movies/detail.html",{'movie': movie})
