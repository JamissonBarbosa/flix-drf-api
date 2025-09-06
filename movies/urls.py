from django.urls import path
from . import views


# URLs
urlpatterns = [
   path('movies/', views.MovieListeCreateView.as_view(), name='movie-create-list'),
    path('movies/<int:pk>/', views.MovieRetriveUpdateDestroyView.as_view(), name='movie-detail'),
    path('movies/stats/', views.MovieStatsView.as_view(), name='movie-stats'),
]