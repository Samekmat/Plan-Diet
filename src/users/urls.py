from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.views.profile import ProfileView
from users.views.register import RegisterView

app_name = "users"

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("register/", RegisterView.as_view(), name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("profile/", ProfileView.as_view(), name="profile"),
]
