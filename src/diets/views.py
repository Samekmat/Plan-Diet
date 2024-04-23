from django.urls import reverse
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from diets.forms import DietModelForm
from diets.models import Diet


class DietListView(ListView):
    model = Diet
    template_name = "diets/diet_list.html"
    context_object_name = "diets"
    paginate_by = 10


class DietDetailView(DetailView):
    model = Diet
    template_name = "diets/diet_detail.html"
    context_object_name = "diet"


class DietCreateView(CreateView):
    form_class = DietModelForm
    template_name = "diets/diet_create.html"

    def get_success_url(self):
        return reverse("diets:diet-detail", kwargs={"pk": self.object.pk})


class DietUpdateView(UpdateView):
    model = Diet
    form_class = DietModelForm
    template_name = "diets/diet_update.html"


class DietDeleteView(DeleteView):
    model = Diet
    template_name = "diets/diet_delete.html"
    success_url = "/diet_list"
