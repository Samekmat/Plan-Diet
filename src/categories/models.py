from django.db import models

from .choices import CATEGORIES


class Category(models.Model):
    name = models.CharField(choices=CATEGORIES, max_length=60)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name
