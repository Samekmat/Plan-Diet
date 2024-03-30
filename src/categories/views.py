from django.shortcuts import render
from django.views import View

from categories.models import Category


class CategoryListView(View):
    def get(self, request):
        categories = Category.objects.all()
        return render(request, 'categories/category_list.html', {'categories': categories})


class CategoryView(View):
    def get(self, request, id):
        category = Category.objects.get(pk=id)
        return render(request, 'categories/category.html', {'category': category})
