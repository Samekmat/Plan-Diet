from django.urls import path

from categories import views

app_name = "categories"


urlpatterns = [
    path("categories/", views.CategoryListView.as_view(), name="categories"),
    path("categories/<int:pk>/", views.CategoryDetailView.as_view(), name="category-detail"),
    path("categories/delete/<int:pk>/", views.CategoryDeleteView.as_view(), name="category-delete"),
    path("categories/create/", views.CategoryCreateView.as_view(), name="category-create"),
    path("categories/update/<int:pk>", views.CategoryUpdateView.as_view(), name="category-update"),
]
