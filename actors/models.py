from django.db import models


NATTIONALITIES_ACTORS = [
  ('USA', 'Estados Unidos'),
  ('UK', 'Reino Unido'),
  ('BR', 'Brasil'),
  ('FR', 'França'),
  ('ES', 'Espanha'),
]
# Create your models here.
class Actor(models.Model):
  name = models.CharField(max_length=200)
  birthday = models.DateField(null=True, blank=True)
  nationality = models.CharField(
    max_length=100, 
    choices=NATTIONALITIES_ACTORS,
    blank=True,
    null=True
  )

  def __str__(self):
    return self.name