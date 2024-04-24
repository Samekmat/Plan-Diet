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
    path("sporttypes/", SportTypeListView.as_view(), name="sporttypes"),
    path("sporttypes/create/", SportTypeCreateView.as_view(), name="sporttype-create"),
    path("sporttypes/<int:pk>/update/", SportTypeUpdateView.as_view(), name="sporttype-update"),
    path("sporttypes/<int:pk>/delete/", SportTypeDeleteView.as_view(), name="sporttype-delete"),
    path("musclegroups/", MuscleGroupListView.as_view(), name="musclegroups"),
    path("musclegroups/create/", MuscleGroupCreateView.as_view(), name="musclegroup-create"),
    path("musclegroups/<int:pk>/update/", MuscleGroupUpdateView.as_view(), name="musclegroup-update"),
    path("musclegroups/<int:pk>/delete/", MuscleGroupDeleteView.as_view(), name="musclegroup-delete"),
]
