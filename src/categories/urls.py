from django.urls import path

from categories import views

app_name = "categories"


urlpatterns = [
    path("categories/", views.CategoryListView.as_view(), name="categories"),
    path("categories/<int:id>/", views.CategoryView.as_view(), name="category-detail"),
    path("categories/delete/<int:id>/", views.CategoryDeleteView.as_view(), name="category-delete"),
    path("categories/create/", views.CategoryCreateView.as_view(), name="category-create"),
]
