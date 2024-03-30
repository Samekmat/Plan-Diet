from django.urls import path

from plans import views

app_name = "plans"


urlpatterns = [
    path("plan_list/", views.PlanListView.as_view(), name="plan-list"),
    path("plan/<int:pk>/", views.PlanView.as_view(), name="plan-detail"),
    path("plan/create/", views.PlanCreateView.as_view(), name="plan-create"),
    path("plan/update/<int:pk>/", views.PlanUpdateView.as_view(), name="plan-update"),
    path("plan/delete/<int:pk>/", views.PlanDeleteView.as_view(), name="plan-delete"),
]
