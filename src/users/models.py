from django.contrib.auth.models import AbstractUser
from django.db import models

from diets.models import Diet
from plandiet_app.choices import SEX
from plans.models import Plan


class CustomUser(AbstractUser):
    username = models.CharField(max_length=24, unique=True)
    age = models.IntegerField(null=True)
    height = models.IntegerField(null=True)
    weight = models.FloatField(null=True)
    sex = models.CharField(choices=SEX, max_length=6)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, null=True)
    diet = models.ForeignKey(Diet, on_delete=models.CASCADE, null=True)
