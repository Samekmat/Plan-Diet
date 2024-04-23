from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            "User data",
            {
                "fields": (
                    "age",
                    "height",
                    "weight",
                    "sex",
                    "plan",
                    "diet",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "email",
                    "first_name",
                    "last_name",
                    "age",
                    "height",
                    "weight",
                    "sex",
                    "password1",
                    "password2",
                ),
            },
        ),
    )


admin.site.register(CustomUser, CustomUserAdmin)
