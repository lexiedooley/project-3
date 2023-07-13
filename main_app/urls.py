from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('movies/<int:movie_id>/', views.movies_detail, name='movies_detail'),
    path('movies/<int:pk>/update/', views.MovieUpdate.as_view(), name='movies_update'),
    path('movies/<int:pk>/delete/', views.MovieDelete.as_view(), name='movies_delete')
    path('movies/' views.movies_index, name='index'),
]

