from django.urls import path

from categories import views

app_name = "categories"


urlpatterns = [
    path('categories/', views.CategoryListView.as_view(), name='categories'),
    path('category/<int:id>/', views.CategoryView.as_view(), name='category-detail'),
    ]
