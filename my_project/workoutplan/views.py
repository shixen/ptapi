from rest_framework import viewsets
from workoutplan.models import WorkoutPlan
from workoutplan.serializers import WorkoutPlanSerializer 

class WorkoutPlanViewSet(viewsets.ModelViewSet):
    queryset = WorkoutPlan.objects.all()
    serializer_class = WorkoutPlanSerializer