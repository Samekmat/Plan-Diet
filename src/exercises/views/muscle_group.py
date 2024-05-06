from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from exercises.models import MuscleGroup


class MuscleGroupListView(ListView):
    model = MuscleGroup
    template_name = "muscles/muscle_group_list.html"
    context_object_name = "muscle_groups"


class MuscleGroupCreateView(CreateView):
    model = MuscleGroup
    template_name = "muscles/muscle_group_form.html"
    fields = ["name"]
    success_url = reverse_lazy("exercises:muscle-groups")


class MuscleGroupUpdateView(UpdateView):
    model = MuscleGroup
    template_name = "muscles/muscle_group_form.html"
    fields = ["name"]
    success_url = reverse_lazy("exercises:muscle-groups")


class MuscleGroupDeleteView(DeleteView):
    model = MuscleGroup
    template_name = "muscles/muscle_group_confirm_delete.html"
    success_url = reverse_lazy("exercises:muscle-groups")
