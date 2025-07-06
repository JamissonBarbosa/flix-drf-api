from django.contrib import admin
from django.urls import path
from genders.views import GenderListCreateView, GenderRetrieveUpdateDestroyView
from actors.views import ActorListCreateView, ActorRetrieveUpdateDestroyView
from movies.views import MovieListeCreateView, MovieRetriveUpdateDestroyView
from reviews.views import ReviewCreateListView, ReviewRetrieveUpdateDestroyView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/api/genders/', GenderListCreateView.as_view(), name='gender-create-list'),
    path('genders/<int:pk>/', GenderRetrieveUpdateDestroyView.as_view(), name='gender-detail'),

    path('api/actors/', ActorListCreateView.as_view(), name='actor-create-list'),
    path('api/actors/<int:pk>/', ActorRetrieveUpdateDestroyView.as_view(), name='actor-detail'),

    path('api/movies/', MovieListeCreateView.as_view(), name='movie-create-list'),
    path('api/movies/<int:pk>/', MovieRetriveUpdateDestroyView.as_view(), name='movie-detail'),

    path('api/reviews/', ReviewCreateListView.as_view(), name='review-create-list'),
    path('api/reviews/<int:pk>/', ReviewRetrieveUpdateDestroyView.as_view(), name='review-detail')
]
