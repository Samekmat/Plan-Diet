from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from exercises.models import SportType


class SportTypeListView(ListView):
    model = SportType
    template_name = "types/sport_type_list.html"
    context_object_name = "sport_types"


class SportTypeCreateView(CreateView):
    model = SportType
    template_name = "types/sport_type_form.html"
    fields = ["name"]
    success_url = reverse_lazy("exercises:sport-types")


class SportTypeUpdateView(UpdateView):
    model = SportType
    template_name = "types/sport_type_form.html"
    fields = ["name"]
    success_url = reverse_lazy("exercises:sport-types")


class SportTypeDeleteView(DeleteView):
    model = SportType
    template_name = "types/sport_type_confirm_delete.html"
    success_url = reverse_lazy("exercises:sport-types")
