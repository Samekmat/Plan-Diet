from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from exercises.models import Exercise


class ExerciseDetailView(DetailView):
    model = Exercise
    template_name = "exercises/exercise_detail.html"
    context_object_name = "exercise"


class ExerciseListView(ListView):
    model = Exercise
    template_name = "exercises/exercise_list.html"
    context_object_name = "exercises"
    paginate_by = 18


class ExerciseCreateView(CreateView):
    model = Exercise
    fields = "__all__"
    template_name = "exercises/exercise_form.html"
    success_url = reverse_lazy("exercises:exercises")


class ExerciseUpdateView(UpdateView):
    model = Exercise
    fields = "__all__"
    template_name = "exercises/exercise_form.html"
    success_url = reverse_lazy("exercises:exercises")


class ExerciseDeleteView(DeleteView):
    model = Exercise
    template_name = "exercises/exercise_confirm_delete.html"
    success_url = reverse_lazy("exercises:exercises")
