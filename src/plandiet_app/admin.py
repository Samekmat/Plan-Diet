from django.contrib import admin

from categories.models import Category
from diets.models import Diet
from exercises.models import MuscleGroup, SportType, Exercise
from plans.models import Plan


admin.site.register(Category)
admin.site.register(MuscleGroup)
admin.site.register(SportType)
admin.site.register(Exercise)
admin.site.register(Diet)
admin.site.register(Plan)
