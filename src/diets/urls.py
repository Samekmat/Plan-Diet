from django.urls import path

from diets import views

app_name = "diets"


urlpatterns = [
    path("diets/list/", views.DietListView.as_view(), name="diet-list"),
    path("diets/<int:pk>/", views.DietDetailView.as_view(), name="diet-detail"),
    path("diets/create/", views.DietCreateView.as_view(), name="diet-create"),
    path("diets/update/<int:pk>/", views.DietUpdateView.as_view(), name="diet-update"),
    path("diets/delete/<int:pk>/", views.DietDeleteView.as_view(), name="diet-delete"),
]
