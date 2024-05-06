from http import HTTPStatus

from django.test import Client, TestCase
from django.urls import reverse

from diets.factories import DietFactory
from exercises.factories import ExerciseFactory
from plans.factories import PlanFactory
from plans.models import Plan


class PlanViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.diet = DietFactory()
        self.exercise = ExerciseFactory()
        self.plan = PlanFactory()

    def test_plan_list_view(self):
        plans = PlanFactory.create_batch(3)

        response = self.client.get(reverse("plans:plans"))

        self.assertEqual(response.status_code, HTTPStatus.OK)

        for plan in plans:
            self.assertIn(plan, response.context["plans"])

        self.assertTemplateUsed(response, "plans/plan_list.html")

    def test_plan_detail_view(self):
        response = self.client.get(reverse("plans:plan-detail", kwargs={"pk": self.plan.pk}))

        self.assertEqual(response.status_code, HTTPStatus.OK)

        self.assertTemplateUsed(response, "plans/plan_detail.html")

        self.assertEqual(response.context["plan"], self.plan)

    def test_plan_create_view(self):
        response = self.client.post(
            reverse("plans:plan-create"),
            {"name": "New Plan", "diet": self.diet.pk, "exercises": [self.exercise.pk]},
        )

        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse("plans:plans"))

        new_plan = Plan.objects.filter(name="New Plan").first()
        self.assertIsNotNone(new_plan)

    def test_plan_update_view(self):
        response = self.client.post(
            reverse("plans:plan-update", kwargs={"pk": self.plan.pk}),
            {"name": "Updated Plan", "diet": self.diet.pk, "exercises": [self.exercise.pk]},
        )

        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse("plans:plans"))

        updated_plan = Plan.objects.get(pk=self.plan.pk)
        self.assertEqual(updated_plan.name, "Updated Plan")

    def test_plan_delete_view(self):
        response = self.client.post(reverse("plans:plan-delete", kwargs={"pk": self.plan.pk}))

        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse("plans:plans"))

        with self.assertRaises(Plan.DoesNotExist):
            Plan.objects.get(pk=self.plan.pk)
