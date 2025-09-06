from rest_framework import generics, views, response, status
from django.db.models import Count, Avg
from rest_framework.permissions import IsAuthenticated
from core.permissions import GlobalDefaultPermission
from movies.models import Movie
from reviews.models import Review
from movies.serializers import MovieModelSerializer, MovieStatsSerializer, MovieListDetailSerializer

class MovieListeCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Movie.objects.all()
    #serializer_class = MovieModelSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovieListDetailSerializer
        return MovieModelSerializer

class MovieRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Movie.objects.all()
    #serializer_class = MovieModelSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovieListDetailSerializer
        return MovieModelSerializer

class MovieStatsView(views.APIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Movie.objects.all()
    
    def get(self, request):
        total_movies = self.queryset.count()
        movies_by_gender = self.queryset.values('gender__name').annotate(count=Count('id'))
        total_reviews = Review.objects.count()
        aversge_star = Review.objects.aggregate(average_star=Avg('star'))['average_star']

        data={
            'total_movies': total_movies,
            'movies_by_gender': movies_by_gender,
            'total_reviews': total_reviews,
            'average_star': round(aversge_star, 1) if aversge_star else 0
            }
        
        serializer = MovieStatsSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        return response.Response(
            data=serializer.validated_data,
            status=status.HTTP_200_OK
        )
        

