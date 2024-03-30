from django.db import models

from categories.models import Category
from exercises.choices import DIFFICULTIES


class MuscleGroup(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class SportType(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Exercise(models.Model):
    name = models.CharField(max_length=124)
    description = models.TextField()
    difficulty = models.CharField(choices=DIFFICULTIES, max_length=60)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, default=None)
    muscles = models.ManyToManyField(MuscleGroup)
    type = models.ManyToManyField(SportType)

    def __str__(self):
        return self.name
