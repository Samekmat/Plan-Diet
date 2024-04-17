from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView, DeleteView, UpdateView

from plans.forms import PlanForm
from plans.models import Plan


class PlanListView(View):
    def get(self, request):
        plans = Plan.objects.all().order_by("pk")
        paginator = Paginator(plans, 5)
        page = request.GET.get("page", 1)
        try:
            pages = paginator.page(page)
        except PageNotAnInteger:
            pages = paginator.page(1)
        except EmptyPage:
            pages = paginator.page(paginator.num_pages)
        return render(request, "plans/plan_list.html", {"plans": plans, "pages": pages})


class PlanDetailView(View):
    def get(self, request, pk):
        plan = Plan.objects.get(pk=pk)
        return render(request, "plans/plan_detail.html", {"plan": plan})


class PlanCreateView(CreateView):
    # PermissionRequiredMixin,
    # permission_required = 'plandiet_app.add_plan'
    form_class = PlanForm
    template_name = "plans/plan_create.html"

    def get_success_url(self):
        return reverse("plans:plan-detail", kwargs={"pk": self.object.pk})


class PlanUpdateView(UpdateView):
    # PermissionRequiredMixin,
    # permission_required = 'plandiet_app.change_plan'
    form_class = PlanForm
    template_name = "plans/plan_update.html"

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Plan, pk=id_)


class PlanDeleteView(DeleteView):
    # PermissionRequiredMixin,
    # permission_required = 'plandiet_app.delete_plan'
    template_name = "plans/plan_delete.html"
    success_url = "/plan_list"

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Plan, pk=id_)
