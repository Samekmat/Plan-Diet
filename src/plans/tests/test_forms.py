from django import forms
from django.test import TestCase

from diets.factories import DietFactory
from exercises.factories import ExerciseFactory
from plans.forms import PlanForm


class PlanFormTest(TestCase):
    def setUp(self):
        self.diet = DietFactory()

        self.exercise1 = ExerciseFactory()
        self.exercise2 = ExerciseFactory()

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
