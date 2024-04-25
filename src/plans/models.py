from django.db import models

from diets.models import Diet
from exercises.models import Exercise


class Plan(models.Model):
    name = models.CharField(max_length=60)
    diet = models.ForeignKey(Diet, on_delete=models.CASCADE, null=True, default=None)
    exercises = models.ManyToManyField(Exercise, default=None)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["pk"]
