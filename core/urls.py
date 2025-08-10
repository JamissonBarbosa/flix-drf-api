from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('api/v1/', include('authentication.urls')),
    path('admin/', admin.site.urls),
    path('api/v1/', include('genders.urls')),
    path('api/v1/', include('actors.urls')),
    path('api/v1/', include('movies.urls')),
    path('api/v1/', include('reviews.urls')),
]
