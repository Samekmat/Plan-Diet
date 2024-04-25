from django.urls import path

from plans import views

app_name = "plans"


urlpatterns = [
    path("plans/", views.PlanListView.as_view(), name="plans"),
    path("plans/<int:pk>/", views.PlanDetailView.as_view(), name="plan-detail"),
    path("plans/create/", views.PlanCreateView.as_view(), name="plan-create"),
    path("plans/update/<int:pk>/", views.PlanUpdateView.as_view(), name="plan-update"),
    path("plans/delete/<int:pk>/", views.PlanDeleteView.as_view(), name="plan-delete"),
]
