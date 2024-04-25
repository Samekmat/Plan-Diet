from django.test import TestCase

from categories.factories import CategoryFactory
from categories.models import Category


class CategoryFactoryTest(TestCase):
    def test_category_factory_creation(self):
        category = CategoryFactory()
        self.assertIsInstance(category, Category)
        self.assertIsNotNone(category.name)
        self.assertIsNotNone(category.description)

    def test_category_factory_with_custom_data(self):
        name = "Custom Category"
        description = "This is a custom category."
        category = CategoryFactory(name=name, description=description)
        self.assertEqual(category.name, name)
        self.assertEqual(category.description, description)

    def test_category_factory_bulk_creation(self):
        categories = CategoryFactory.create_batch(5)
        self.assertEqual(len(categories), 5)
        for category in categories:
            self.assertIsInstance(category, Category)
