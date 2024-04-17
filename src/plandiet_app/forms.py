from django import forms

from plandiet_app.choices import ACTIVITY, GOAL, SEX


class MacroCalculatorForm(forms.Form):
    age = forms.IntegerField(label="Age", widget=forms.NumberInput(attrs={"class": "form-control"}))
    height = forms.IntegerField(label="Height", widget=forms.NumberInput(attrs={"class": "form-control"}))
    weight = forms.FloatField(label="Weight", widget=forms.NumberInput(attrs={"class": "form-control"}))
    sex = forms.ChoiceField(label="Sex", choices=SEX, widget=forms.Select(attrs={"class": "form-control"}))
    activity = forms.ChoiceField(
        label="Activity", choices=ACTIVITY, widget=forms.Select(attrs={"class": "form-control"})
    )
    goal = forms.ChoiceField(label="Goal", choices=GOAL, widget=forms.Select(attrs={"class": "form-control"}))

    def clean_age(self):
        age = self.cleaned_data.get("age")
        if age is not None and age <= 0:
            raise forms.ValidationError("Age must be a positive number.")
        return age

    def clean_height(self):
        height = self.cleaned_data.get("height")
        if height is not None and height <= 0:
            raise forms.ValidationError("Height must be a positive number.")
        return height

    def clean_weight(self):
        weight = self.cleaned_data.get("weight")
        if weight is not None and weight <= 0:
            raise forms.ValidationError("Weight must be a positive number.")
        return weight
