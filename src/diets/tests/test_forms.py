from django.test import TestCase

from diets.forms import DietModelForm


class DietFormTest(TestCase):
    def test_diet_form_valid_data(self):
        form_data = {
            "name": "Test Diet",
            "caloric_demand": 2000,
            "carbs_demand": 300,
            "protein_demand": 150,
            "fat_demand": 70,
            "description": "This is a test diet description.",
        }
        form = DietModelForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_diet_form_invalid_data(self):
        form_data = {
            "name": "",
            "caloric_demand": 2000,
            "carbs_demand": 300,
            "protein_demand": 150,
            "fat_demand": 70,
            "description": "This is a test diet description.",
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
