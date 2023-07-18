from django.shortcuts import render
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import Movie

# Create your views here.
def home(request):
    return render(request, 'home.html')


class MovieUpdate(UpdateView):
    model = Movie
    fields = ['year', 'genre', 'rating', 'description']

class MovieDelete(DeleteView):
    model = Movie
    success_url = '/allmovies'

def movies_index(request):
    movies = Movie.objects.all()
    return render(request, 'movies/index.html',
                  {
                      'movies': movies
                  })
class MovieCreate(CreateView):
    model = Movie
    fields = '__all__'
    

def movies_detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, 'movies/detail.html', {
        'movie' : movie
    })


