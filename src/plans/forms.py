from django import forms

from .models import Plan


class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = ["name", "diet", "exercises"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "diet": forms.Select(attrs={"class": "form-control"}),
            "exercises": forms.SelectMultiple(attrs={"class": "form-control"}),
        }
