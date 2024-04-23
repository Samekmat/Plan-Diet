from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import CreateView

from users.forms import CustomUserCreationForm, LoginForm
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


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data["password1"])
        user.save()
        return super().form_valid(form)


class ProfileView(View):
    def get(self, request):
        if CustomUser.is_authenticated:
            current_user = request.user
            return render(request, "users/profile.html", {"current_user": current_user})
        return render(request, "users/profile.html")
