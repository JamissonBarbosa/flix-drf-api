from rest_framework import serializers
from django.db.models import Avg
from actors.serializers import ActorSerializer
from movies.models import Movie
from genders.models import Gender
from genders.serializers import GenderSerializer
from actors.models import Actor


#Teste de exemplo de Serializer
class MovieSerializers(serializers.Serializer):
  id = serializers.IntegerField()
  title = serializers.CharField()
  gender = serializers.PrimaryKeyRelatedField(queryset=Gender.objects.all())
  release_date = serializers.DateField()
  actors = serializers.PrimaryKeyRelatedField(queryset=Actor.objects.all(), many=True)
  resume = serializers.CharField()

class MovieModelSerializer(serializers.ModelSerializer):

  class Meta:
    model = Movie
    fields = '__all__'
  
  def validate_release_date(self, value):
    if value.year < 1900:
      raise serializers.ValidationError('O ano de lançamento deve ser maior que 1900')
    return value
  
  def validate_resume(self, value):
    if len(value) > 300:
      raise serializers.ValidationError('O resumo deve ter no máximo 200 caracteres')
    return value
  
class MovieListDetailSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True)
    gender = GenderSerializer()
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'gender', 'release_date', 'actors', 'resume', 'rate']
    
    def get_rate(self, obj):
      rate = obj.reviews.aggregate(Avg('star'))['star__avg']
      if rate:
        return round(rate, 1)
      return None
        

class MovieStatsSerializer(serializers.Serializer):
  total_movies = serializers.IntegerField()
  movies_by_gender = serializers.ListField()
  total_reviews = serializers.IntegerField()
  average_star = serializers.FloatField()