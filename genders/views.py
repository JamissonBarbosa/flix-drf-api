from genders.models import Gender
from rest_framework import generics
from genders.serializers import GenderSerializer


# Create your views here.
class GenderListCreateView(generics.ListCreateAPIView):
    queryset = Gender.objects.all()
    serializer_class = GenderSerializer

class GenderRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Gender.objects.all()
    serializer_class = GenderSerializer