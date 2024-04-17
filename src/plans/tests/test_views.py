from django.test import Client, TestCase
from django.urls import reverse

from diets.models import Diet
from exercises.models import Exercise, MuscleGroup, SportType
from plans.models import Plan
from users.models import CustomUser as User


class PlanViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.client = Client()

        self.muscle_group = MuscleGroup.objects.create(name="Legs")
        self.sport_type = SportType.objects.create(name="Cardio")

        self.exercise = Exercise.objects.create(name="Squats", description="Test Description", difficulty="beginner")
        self.exercise.muscles.add(self.muscle_group)
        self.exercise.type.add(self.sport_type)

        self.diet = Diet.objects.create(
            name="Test Diet",
            caloric_demand=2700,
            carbs_demand=150,
            protein_demand=120,
            fat_demand=90,
            description="Test desc",
        )

        self.plan = Plan.objects.create(name="Test Plan", diet=self.diet)
        self.plan.exercises.add(self.exercise)

    def test_plan_list_view(self):
        response = self.client.get(reverse("plans:plan-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "plans/plan_list.html")
        self.assertContains(response, self.plan.name)

    def test_plan_detail_view(self):
        response = self.client.get(reverse("plans:plan-detail", kwargs={"pk": self.plan.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "plans/plan_detail.html")
        self.assertContains(response, self.plan.name)

    def test_plan_create_view(self):
        self.client.login(username="testuser", password="testpassword")
        response = self.client.post(
            reverse("plans:plan-create"), {"name": "New Plan", "diet": self.diet.id, "exercises": [self.exercise.id]}
        )
        self.assertEqual(response.status_code, 302)

        new_plan = Plan.objects.filter(name="New Plan").first()
        self.assertIsNotNone(new_plan)

    def test_plan_update_view(self):
        self.client.login(username="testuser", password="testpassword")
        response = self.client.post(
            reverse("plans:plan-update", kwargs={"pk": self.plan.pk}),
            {"name": "Updated Plan", "diet": self.diet.id, "exercises": [self.exercise.id]},
        )
        self.assertEqual(response.status_code, 302)

        redirect_url = response.url
        response = self.client.get(redirect_url)
        self.assertEqual(response.status_code, 200)
        updated_plan = Plan.objects.get(pk=self.plan.pk)
        self.assertEqual(updated_plan.name, "Updated Plan")

    def test_plan_delete_view(self):
        self.client.login(username="testuser", password="testpassword")
        response = self.client.post(reverse("plans:plan-delete", kwargs={"pk": self.plan.pk}))
        self.assertEqual(response.status_code, 302)
        with self.assertRaises(Plan.DoesNotExist):
            Plan.objects.get(pk=self.plan.pk)
