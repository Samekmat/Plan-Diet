from django.test import TestCase

from diets.factories import DietFactory
from diets.forms import DietModelForm


class DietFormTest(TestCase):
    def setUp(self):
        self.diet = DietFactory()

    def test_diet_form_valid_data(self):
        form_data = {
            "name": self.diet.name,
            "caloric_demand": self.diet.caloric_demand,
            "carbs_demand": self.diet.carbs_demand,
            "protein_demand": self.diet.protein_demand,
            "fat_demand": self.diet.fat_demand,
            "description": self.diet.description,
        }
        form = DietModelForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_diet_form_invalid_data(self):
        form_data = {
            "name": "",
            "caloric_demand": self.diet.caloric_demand,
            "carbs_demand": self.diet.carbs_demand,
            "protein_demand": self.diet.protein_demand,
            "fat_demand": self.diet.fat_demand,
            "description": self.diet.description,
        }
        form = DietModelForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_diet_form_widgets(self):
        form = DietModelForm()
        self.assertIn('class="form-control"', str(form["name"]))
        self.assertIn('class="form-control"', str(form["description"]))
        self.assertIn('class="form-control"', str(form["caloric_demand"]))
        self.assertIn('class="form-control"', str(form["carbs_demand"]))
        self.assertIn('class="form-control"', str(form["protein_demand"]))
        self.assertIn('class="form-control"', str(form["fat_demand"]))
