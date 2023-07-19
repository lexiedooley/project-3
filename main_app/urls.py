from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('movies/<int:movie_id>/', views.movies_detail, name='movies_detail'),
    path('movies/<int:pk>/update/', views.MovieUpdate.as_view(), name='movies_update'),
    path('movies/<int:pk>/delete/', views.MovieDelete.as_view(), name='movies_delete'),
    path('allmovies/', views.movies_index, name='index'),
    path('movies/create/', views.MovieCreate.as_view(), name='movies_create'),
    path('search/', views.search_results, name='search_results'),
]

