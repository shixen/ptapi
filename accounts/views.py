from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer

class SignupViewSet(viewsets.GenericViewSet, viewsets.mixins.CreateModelMixin):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]