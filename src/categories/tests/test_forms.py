from django.test import TestCase

from categories.forms import CategoryForm


class CategoryFormTest(TestCase):
    def test_category_form_valid_data(self):
        form_data = {"name": "Test category", "description": "This is a test category."}
        form = CategoryForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_category_form_invalid_data(self):
        form_data = {"name": "", "description": "This is a test category."}
        form = CategoryForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_category_form_widgets(self):
        form = CategoryForm()
        self.assertIn('class="form-control"', str(form["name"]))
        self.assertIn('class="form-control"', str(form["description"]))
        self.assertIn('rows="3"', str(form["description"]))
