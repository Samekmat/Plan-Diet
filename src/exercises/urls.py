from django.urls import path

from exercises.views.exercise import (
    ExerciseCreateView,
    ExerciseDeleteView,
    ExerciseDetailView,
    ExerciseListView,
    ExerciseUpdateView,
)
from exercises.views.muscle_group import (
    MuscleGroupCreateView,
    MuscleGroupDeleteView,
    MuscleGroupListView,
    MuscleGroupUpdateView,
)
from exercises.views.sport_type import (
    SportTypeCreateView,
    SportTypeDeleteView,
    SportTypeListView,
    SportTypeUpdateView,
)

app_name = "exercises"


urlpatterns = [
    path("exercise/<int:pk>/", ExerciseDetailView.as_view(), name="exercise-detail"),
    path("exercises/", ExerciseListView.as_view(), name="exercises"),
    path("exercise/create/", ExerciseCreateView.as_view(), name="exercise-create"),
    path("exercise/<int:pk>/update/", ExerciseUpdateView.as_view(), name="exercise-update"),
    path("exercise/<int:pk>/delete/", ExerciseDeleteView.as_view(), name="exercise-delete"),
    path("sporttypes/", SportTypeListView.as_view(), name="sport-types"),
    path("sport-types/create/", SportTypeCreateView.as_view(), name="sport-type-create"),
    path("sport-types/<int:pk>/update/", SportTypeUpdateView.as_view(), name="sport-type-update"),
    path("sport-types/<int:pk>/delete/", SportTypeDeleteView.as_view(), name="sport-type-delete"),
    path("muscle-groups/", MuscleGroupListView.as_view(), name="muscle-groups"),
    path("muscle-groups/create/", MuscleGroupCreateView.as_view(), name="muscle-group-create"),
    path("muscle-groups/<int:pk>/update/", MuscleGroupUpdateView.as_view(), name="muscle-group-update"),
    path("muscle-groups/<int:pk>/delete/", MuscleGroupDeleteView.as_view(), name="muscle-group-delete"),
]
