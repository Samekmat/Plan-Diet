from django.test import TestCase

from diets.factories import DietFactory
from exercises.factories import ExerciseFactory
from plans.factories import PlanFactory
from plans.models import Plan


class PlanFactoryTestCase(TestCase):
    def test_plan_factory_creation(self):
        diet = DietFactory()

        exercises = ExerciseFactory.create_batch(3)

        plan = PlanFactory(diet=diet)
        plan.exercises.set(exercises)

        self.assertIsInstance(plan, Plan)

        self.assertEqual(plan.diet, diet)

        self.assertCountEqual(plan.exercises.all(), exercises)

    def test_plan_bulk_create(self):
        plans = PlanFactory.create_batch(5)

        self.assertEqual(Plan.objects.count(), 5)

        for plan in plans:
            self.assertIsInstance(plan, Plan)
