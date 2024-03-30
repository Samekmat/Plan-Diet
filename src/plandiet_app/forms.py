from django import forms

from plandiet_app.choices import ACTIVITY, GOAL, SEX


class MacroCalculatorForm(forms.Form):
    age = forms.IntegerField(label='Age', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    height = forms.IntegerField(label='Height', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    weight = forms.FloatField(label='Weight', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    sex = forms.ChoiceField(label='Sex', choices=SEX, widget=forms.Select(attrs={'class': 'form-control'}))
    activity = forms.ChoiceField(label='Activity', choices=ACTIVITY, widget=forms.Select(attrs={'class': 'form-control'}))
    goal = forms.ChoiceField(label='Goal', choices=GOAL, widget=forms.Select(attrs={'class': 'form-control'}))
