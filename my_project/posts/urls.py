from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, WorkoutPlanViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'workoutplans', WorkoutPlanViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]