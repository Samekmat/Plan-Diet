from django.contrib import admin
from .forms import CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'User data',
            {
                'fields': (
                    'age',
                    'height',
                    'weight',
                    'sex',
                    'plan',
                    'diet',

                )
            }
        )
    )


admin.site.register(CustomUser, CustomUserAdmin)
