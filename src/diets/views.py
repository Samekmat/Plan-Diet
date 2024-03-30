from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView, DeleteView, UpdateView

from diets.forms import DietModelForm
from diets.models import Diet


class DietListView(View):
    def get(self, request):
        diets = Diet.objects.all()
        paginator = Paginator(diets, 10)
        page = request.GET.get("page", 1)
        try:
            pages = paginator.page(page)
        except PageNotAnInteger:
            pages = paginator.page(1)
        except EmptyPage:
            pages = paginator.page(paginator.num_pages)
        return render(request, "diets/diet_list.html", {"diets": diets, "pages": pages})


class DietView(View):
    def get(self, request, pk):
        diet = Diet.objects.get(pk=pk)

        return render(request, "diets/diet.html", {"diet": diet})


class DietCreateView(CreateView):
    # PermissionRequiredMixin,
    # permission_required = 'plandiet_app.add_diet'
    form_class = DietModelForm
    template_name = "diets/diet_create.html"

    def get_success_url(self):
        return reverse("diets:diet-detail", kwargs={"pk": self.object.pk})


class DietUpdateView(UpdateView):
    # PermissionRequiredMixin,
    # permission_required = 'plandiet_app.change_diet'
    form_class = DietModelForm
    template_name = "diets/diet_update.html"

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Diet, pk=id_)


class DietDeleteView(DeleteView):
    # PermissionRequiredMixin,
    # permission_required = 'plandiet_app.delete_diet'
    template_name = "diets/diet_delete.html"
    success_url = "/diet_list"

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Diet, pk=id_)
