from django.core.paginator import Page
from django.test import TestCase
from django.urls import reverse

from diets.models import Diet


class DietViewsTest(TestCase):
    def setUp(self):
        for diet_num in range(20):
            Diet.objects.create(
                name=f"Diet {diet_num}",
                description=f"Description {diet_num}",
                caloric_demand=2500,
                carbs_demand=160,
                protein_demand=150,
                fat_demand=90,
            )
        self.diet = Diet.objects.first()

    def test_diet_list_view(self):
        response = self.client.get(reverse("diets:diet-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "diets/diet_list.html")
        self.assertTrue("pages" in response.context)
        self.assertIsInstance(response.context["pages"], Page)
        self.assertEqual(len(response.context["pages"].object_list), 10)

    def test_diet_detail_view(self):
        response = self.client.get(reverse("diets:diet-detail", args=(self.diet.pk,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "diets/diet.html")
        self.assertTrue("diet" in response.context)
        self.assertEqual(response.context["diet"], self.diet)

    def test_diet_create_view(self):
        data = {
            "name": "New Diet",
            "description": "New Description",
            "caloric_demand": 3200,
            "carbs_demand": 160,
            "protein_demand": 165,
            "fat_demand": 100,
        }
        response = self.client.post(reverse("diets:diet-create"), data=data)
        self.assertEqual(response.status_code, 302)

    def test_diet_update_view(self):
        updated_data = {
            "name": "Updated Diet",
            "description": "Updated Description",
            "caloric_demand": 3200,
            "carbs_demand": 160,
            "protein_demand": 165,
            "fat_demand": 100,
        }
        response = self.client.post(reverse("diets:diet-update", args=(self.diet.pk,)), data=updated_data)
        self.assertEqual(response.status_code, 302)
        self.diet.refresh_from_db()
        self.assertEqual(self.diet.name, "Updated Diet")
        self.assertEqual(self.diet.description, "Updated Description")
        self.assertEqual(self.diet.caloric_demand, 3200)

    def test_diet_delete_view(self):
        response = self.client.post(reverse("diets:diet-delete", args=(self.diet.pk,)))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Diet.objects.filter(pk=self.diet.pk).exists())
