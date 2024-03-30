from django import forms

from diets.models import Diet


class DietModelForm(forms.ModelForm):
    class Meta:
        model = Diet
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'caloric_demand': forms.NumberInput(attrs={'class': 'form-control'}),
            'carbs_demand': forms.NumberInput(attrs={'class': 'form-control'}),
            'protein_demand': forms.NumberInput(attrs={'class': 'form-control'}),
            'fat_demand': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }
