from django.shortcuts import render
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import Movie
from django import forms

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

class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=True)

def search_results(request):
    form = SearchForm(request.GET)
    if form.is_valid():
        query = form.cleaned_data['query']
        movie = Movie.objects.get(title__icontains=query)
    else:
        movie = []
    return render(request, 'search_results.html', {
        'movie': movie 
        })