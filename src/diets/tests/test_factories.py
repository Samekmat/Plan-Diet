from django.test import TestCase

from diets.factories import DietFactory
from diets.models import Diet


class DietFactoryTest(TestCase):
    def test_diet_factory_creation(self):
        diet = DietFactory()
        self.assertIsInstance(diet, Diet)
        self.assertIsNotNone(diet.name)
        self.assertIsNotNone(diet.caloric_demand)
        self.assertIsNotNone(diet.carbs_demand)
        self.assertIsNotNone(diet.protein_demand)
        self.assertIsNotNone(diet.fat_demand)
        self.assertIsNotNone(diet.description)

    def test_diet_factory_with_custom_data(self):
        name = "Custom Diet"
        caloric_demand = 2000
        carbs_demand = 100
        protein_demand = 150
        fat_demand = 70
        description = "This is a custom diet."
        diet = DietFactory(
            name=name,
            caloric_demand=caloric_demand,
            carbs_demand=carbs_demand,
            protein_demand=protein_demand,
            fat_demand=fat_demand,
            description=description,
        )
        self.assertEqual(diet.name, name)
        self.assertEqual(diet.caloric_demand, caloric_demand)
        self.assertEqual(diet.carbs_demand, carbs_demand)
        self.assertEqual(diet.protein_demand, protein_demand)
        self.assertEqual(diet.fat_demand, fat_demand)
        self.assertEqual(diet.description, description)

    def test_diet_factory_bulk_creation(self):
        diets = DietFactory.create_batch(5)
        self.assertEqual(len(diets), 5)
        for diet in diets:
            self.assertIsInstance(diet, Diet)
