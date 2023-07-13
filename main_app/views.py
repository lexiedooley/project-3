from django.shortcuts import render
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import Movie

# Create your views here.
def home(request):
    return render(request, 'home.html')


class MovieCreate(UpdateView):
    model = Movie
    fields = ['year', 'genre', 'rating', 'description']

class MovieCreate(DeleteView):
    model = Movie
    success_url = '/movies'

def movies_index(request):
    movies = Movie.objects.all()
    return render(request, 'movies/index.html',
                  {
                      'movies': movies
                  })
class MovieCreate(CreateView):
    model = Movie
    fields = '__all__'
    success_url = '/movies/{movie_id}'


