from django.shortcuts import render
from rest_framework import viewsets
from .models import posts, WorkoutPlan
from .serializers import PostSerializer, WorkoutPlanSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class WorkoutPlanViewSet(viewsets.ModelViewSet):
    queryset = WorkoutPlan.objects.all()
    serializer_class = WorkoutPlanSerializer