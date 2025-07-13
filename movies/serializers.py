from rest_framework import serializers
from django.db.models import Avg
from movies.models import Movie
from genders.models import Gender
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
  rate = serializers.SerializerMethodField(read_only=True)

  class Meta:
    model = Movie
    fields = '__all__'

  def get_rate(self, obj):
    rate = obj.reviews.aggregate(Avg('star'))['star__avg']
    if rate:
      return round(rate, 1)
    return None
    # reviews = obj.reviews.all()
    # if reviews:
    #   sum_reviews = 0
    #   for review in reviews:
    #     sum_reviews += review.star
    #     reviews_count = reviews.count()
    #     return round(sum_reviews / reviews_count, 1)
    # return None
  
  def validate_release_date(self, value):
    if value.year < 1900:
      raise serializers.ValidationError('O ano de lançamento deve ser maior que 1900')
    return value
  
  def validate_resume(self, value):
    if len(value) > 300:
      raise serializers.ValidationError('O resumo deve ter no máximo 200 caracteres')
    return value