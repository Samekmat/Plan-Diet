from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from exercises.models import SportType


class SportTypeListView(ListView):
    model = SportType
    template_name = "types/sporttype_list.html"
    context_object_name = "sporttypes"


class SportTypeCreateView(CreateView):
    model = SportType
    template_name = "types/sporttype_form.html"
    fields = ["name"]
    success_url = reverse_lazy("exercises:sporttypes")


class SportTypeUpdateView(UpdateView):
    model = SportType
    template_name = "types/sporttype_form.html"
    fields = ["name"]
    success_url = reverse_lazy("exercises:sporttypes")


class SportTypeDeleteView(DeleteView):
    model = SportType
    template_name = "types/sporttype_confirm_delete.html"
    success_url = reverse_lazy("exercises:sporttypes")
