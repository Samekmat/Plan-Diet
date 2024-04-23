from django.urls import path

from exercises import views

app_name = "exercises"


urlpatterns = [
    path("exercise/<int:pk>/", views.ExerciseDetailView.as_view(), name="exercise-detail"),
    path("exercises/", views.ExerciseListView.as_view(), name="exercise-list"),
    path("exercise/create/", views.ExerciseCreateView.as_view(), name="exercise-create"),
    path("exercise/<int:pk>/update/", views.ExerciseUpdateView.as_view(), name="exercise-update"),
    path("exercise/<int:pk>/delete/", views.ExerciseDeleteView.as_view(), name="exercise-delete"),
]
