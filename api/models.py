# api/models.py
from django.db import models
from tastypie.resources import ModelResource
from movies.models import Movie

# Create your models here.
class MovieResource(ModelResource):
    class Meta: # tastypie looks for this meta details
        queryset = Movie.objects.all()
        resource_name = 'movies' # urls will automatically be created using this name

