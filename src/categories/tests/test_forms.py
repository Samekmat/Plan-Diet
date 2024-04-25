from django.test import TestCase

from categories.factories import CategoryFactory
from categories.forms import CategoryForm


class CategoryFormTest(TestCase):
    def test_category_form_valid_data(self):
        category = CategoryFactory()
        form = CategoryForm(data={"name": category.name, "description": category.description})
        self.assertTrue(form.is_valid())

    def test_category_form_invalid_data(self):
        category = CategoryFactory(name="")
        form = CategoryForm(data={"name": category.name, "description": category.description})
        self.assertFalse(form.is_valid())

    def test_category_form_widgets(self):
        form = CategoryForm()
        self.assertIn('class="form-control"', str(form["name"]))
        self.assertIn('class="form-control"', str(form["description"]))
        self.assertIn('rows="3"', str(form["description"]))
