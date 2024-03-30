from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from django.views.generic import FormView

from users.forms import LoginForm, RegistrationForm
from users.models import CustomUser


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, "registration/login.html", {"form": form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data["login"], password=form.cleaned_data["password"])
            if user:
                login(request, user)
                return redirect("index")
            else:
                return render(request, "registration/login.html", {"form": form, "error": "User can't be found"})


class LogoutView(View):
    def get(self, request):
        logout(request)
        # return redirect(request.META['HTTP_REFERER'])
        return redirect(reverse("index"))


class RegistrationFormView(FormView):
    def get(self, request):
        form = RegistrationForm()
        return render(request, "registration/register.html", {"form": form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            CustomUser.objects.create_user(
                username=form.cleaned_data["username"],
                first_name=form.cleaned_data["first_name"],
                last_name=form.cleaned_data["last_name"],
                password=form.cleaned_data["password1"],
                email=form.cleaned_data["email"],
                age=form.cleaned_data["age"],
                height=form.cleaned_data["height"],
                weight=form.cleaned_data["weight"],
                sex=form.cleaned_data["sex"],
            )
            return redirect("login")
        return render(request, "registration/register.html", {"form": form})


class ProfileView(View):
    def get(self, request):
        if CustomUser.is_authenticated:
            current_user = request.user
            return render(request, "users/profile.html", {"current_user": current_user})
        return render(request, "users/profile.html")
