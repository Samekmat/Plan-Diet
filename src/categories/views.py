from django.shortcuts import redirect, render
from django.views import View

from categories.forms import CategoryForm
from categories.models import Category


class CategoryListView(View):
    def get(self, request):
        categories = Category.objects.all()
        return render(request, "categories/category_list.html", {"categories": categories})


class CategoryView(View):
    def get(self, request, id):
        category = Category.objects.get(pk=id)
        return render(request, "categories/category_detail.html", {"category": category})


class CategoryCreateView(View):
    def get(self, request):
        form = CategoryForm()
        return render(request, "categories/category_create.html", {"form": form})

    def post(self, request):
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("categories:categories")
        return render(request, "categories/category_create.html", {"form": form})


class CategoryDeleteView(View):
    def get(self, request, id):
        category = Category.objects.get(pk=id)
        return render(request, "categories/category_confirm_delete.html", {"category": category})

    def post(self, request, id):
        category = Category.objects.get(pk=id)
        category.delete()
        return redirect("categories:categories")
