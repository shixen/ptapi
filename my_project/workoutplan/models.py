from django.db import models

class WorkoutPlan(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    exercises = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
