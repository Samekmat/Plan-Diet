from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models

from diets.models import Diet
from plandiet_app.choices import SEX
from plans.models import Plan


class CustomUser(AbstractUser):
    username = models.CharField(max_length=24, unique=True)
    age = models.PositiveIntegerField(null=True)
    height = models.PositiveIntegerField(null=True)
    weight = models.FloatField(null=True)
    sex = models.CharField(choices=SEX, max_length=6)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, null=True)
    diet = models.ForeignKey(Diet, on_delete=models.CASCADE, null=True)

    def save(self, *args, **kwargs):
        if self.age is not None and self.age <= 0:
            raise ValidationError("Age must be a positive number.")
        if self.height is not None and self.height <= 0:
            raise ValidationError("Height must be a positive number.")
        if self.weight is not None and self.weight <= 0:
            raise ValidationError("Weight must be a positive number.")
