from django.urls import path

from exercises import views

app_name = "exercises"


urlpatterns = [
    path('exercise/<int:id>/', views.ExerciseView.as_view(), name='exercise-detail'),
    path('exercise_list/', views.ExerciseListView.as_view(), name='exercise-list'),
    ]
