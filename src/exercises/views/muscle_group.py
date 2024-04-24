from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from exercises.models import MuscleGroup


class MuscleGroupListView(ListView):
    model = MuscleGroup
    template_name = "muscles/musclegroup_list.html"
    context_object_name = "musclegroups"


class MuscleGroupCreateView(CreateView):
    model = MuscleGroup
    template_name = "muscles/musclegroup_form.html"
    fields = ["name"]
    success_url = reverse_lazy("exercises:musclegroups")


class MuscleGroupUpdateView(UpdateView):
    model = MuscleGroup
    template_name = "muscles/musclegroup_form.html"
    fields = ["name"]
    success_url = reverse_lazy("exercises:musclegroups")


class MuscleGroupDeleteView(DeleteView):
    model = MuscleGroup
    template_name = "muscles/musclegroup_confirm_delete.html"
    success_url = reverse_lazy("exercises:musclegroups")
