from django import forms
from django.test import TestCase

from diets.models import Diet
from exercises.models import Exercise
from plans.forms import PlanForm


class PlanFormTest(TestCase):
    def setUp(self):
        self.diet = Diet.objects.create(
            name="Test Diet",
            caloric_demand=2700,
            carbs_demand=150,
            protein_demand=120,
            fat_demand=90,
            description="Test desc",
        )
        self.exercise1 = Exercise.objects.create(name="Test Exercise 1")
        self.exercise2 = Exercise.objects.create(name="Test Exercise 2")

    def test_form_fields(self):
        form = PlanForm()
        self.assertIn("name", form.fields)
        self.assertIn("diet", form.fields)
        self.assertIn("exercises", form.fields)

    def test_form_widgets(self):
        form = PlanForm()
        self.assertIsInstance(form.fields["name"].widget, forms.TextInput)
        self.assertIsInstance(form.fields["diet"].widget, forms.Select)
        self.assertIsInstance(form.fields["exercises"].widget, forms.SelectMultiple)

    def test_form_valid_data(self):
        form_data = {"name": "Test Plan", "diet": self.diet.pk, "exercises": [self.exercise1.pk, self.exercise2.pk]}
        form = PlanForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid_data(self):
        form_data = {"name": "", "diet": "", "exercises": ""}
        form = PlanForm(data=form_data)
        self.assertFalse(form.is_valid())
