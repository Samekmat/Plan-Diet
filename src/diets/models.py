from django.db import models
from django.urls import reverse


class Diet(models.Model):
    name = models.CharField(max_length=124)
    caloric_demand = models.IntegerField()
    carbs_demand = models.IntegerField()
    protein_demand = models.IntegerField()
    fat_demand = models.IntegerField()
    description = models.TextField()

    def get_absolute_url(self):
        return reverse("diets:diet-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["pk"]
