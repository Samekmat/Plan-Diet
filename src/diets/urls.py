from django.urls import path

from diets import views

app_name = "diets"


urlpatterns = [
    path('diet_list/', views.DietListView.as_view(), name='diet-list'),
    path('diet/<int:pk>/', views.DietView.as_view(), name='diet'),
    path('diet/add/', views.DietCreateView.as_view(), name='diet-add'),
    path('diet/update/<int:pk>/', views.DietUpdateView.as_view(), name='diet-update'),
    path('diet/delete/<int:pk>/', views.DietDeleteView.as_view(), name='diet-delete'),
]