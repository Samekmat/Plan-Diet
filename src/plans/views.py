from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from plans.forms import PlanForm
from plans.models import Plan


class PlanListView(ListView):
    model = Plan
    template_name = "plans/plan_list.html"
    context_object_name = "plans"
    paginate_by = 5


class PlanDetailView(DetailView):
    model = Plan
    template_name = "plans/plan_detail.html"
    context_object_name = "plan"


class PlanCreateView(CreateView):
    model = Plan
    form_class = PlanForm
    template_name = "plans/plan_create.html"
    success_url = reverse_lazy("plans:plans")


class PlanUpdateView(UpdateView):
    model = Plan
    form_class = PlanForm
    template_name = "plans/plan_update.html"
    success_url = reverse_lazy("plans:plans")


class PlanDeleteView(DeleteView):
    model = Plan
    template_name = "plans/plan_delete.html"
    success_url = reverse_lazy("plans:plans")
