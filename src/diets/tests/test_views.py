from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from diets.factories import DietFactory
from diets.models import Diet


class DietViewsTest(TestCase):
    def setUp(self):
        self.diet = DietFactory()

    def test_diet_list_view(self):
        response = self.client.get(reverse("diets:diets"))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertIn(self.diet, response.context_data["diets"])

    def test_diet_detail_view(self):
        response = self.client.get(reverse("diets:diet-detail", kwargs={"pk": self.diet.pk}))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data["diet"], self.diet)

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
        created_diet_pk = response.url.split("/")[-2]
        expected_redirect_url = reverse("diets:diet-detail", kwargs={"pk": created_diet_pk})

        self.assertRedirects(response, expected_redirect_url)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

    def test_diet_update_view(self):
        expected_redirect_url = reverse("diets:diet-detail", kwargs={"pk": self.diet.pk})
        updated_data = {
            "name": "Updated Diet",
            "description": "Updated Description",
            "caloric_demand": 3200,
            "carbs_demand": 160,
            "protein_demand": 165,
            "fat_demand": 100,
        }
        response = self.client.post(reverse("diets:diet-update", args=(self.diet.pk,)), data=updated_data)
        self.assertRedirects(response, expected_redirect_url)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.diet.refresh_from_db()
        self.assertEqual(self.diet.name, updated_data["name"])
        self.assertEqual(self.diet.description, updated_data["description"])
        self.assertEqual(self.diet.caloric_demand, updated_data["caloric_demand"])

    def test_diet_delete_view(self):
        expected_redirect_url = reverse("diets:diets")
        response = self.client.post(reverse("diets:diet-delete", args=(self.diet.pk,)))
        self.assertRedirects(response, expected_redirect_url)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertFalse(Diet.objects.filter(pk=self.diet.pk).exists())
