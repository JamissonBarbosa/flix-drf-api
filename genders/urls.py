from django.urls import path
from . import views

# URLs
urlpatterns = [
    path('genders/', views.GenderListCreateView.as_view(), name='gender-create-list'),
    path('genders/<int:pk>/', views.GenderRetrieveUpdateDestroyView.as_view(), name='gender-detail'),
]