from django.contrib import admin
from genders.models import Gender

# Register your models here.
@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
  list_display = ('id', 'name')