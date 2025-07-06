from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from movies.models import Movie

# Create your models here.
class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT, related_name='reviews')
    star = models.IntegerField(validators=[
            MinValueValidator(1, 'Avaliação não pode ser menor que 0 estrelas'), 
            MaxValueValidator(5, 'Avaliação não pode ser maior que 5 estrelas')
        ]
    )
    comment = models.TextField(null=True, blank=True)