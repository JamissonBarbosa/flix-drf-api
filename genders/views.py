from rest_framework.permissions import IsAuthenticated
from core.permissions import GlobalDefaultPermission
from rest_framework import generics
from genders.models import Gender
from genders.serializers import GenderSerializer
#from genders.permissions import GenderPermissionClass


# Create your views here.
class GenderListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Gender.objects.all()
    serializer_class = GenderSerializer

class GenderRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Gender.objects.all()
    serializer_class = GenderSerializer