from django.test import RequestFactory, TestCase
from django.urls import reverse

from diets.factories import DietFactory
from diets.models import Diet
from diets.views import (
    DietCreateView,
    DietDeleteView,
    DietDetailView,
    DietListView,
    DietUpdateView,
)


class DietViewsTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.diet = DietFactory()

    def test_diet_list_view(self):
        request = self.factory.get(reverse("diets:diets"))
        response = DietListView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.diet, response.context_data["diets"])

    def test_diet_detail_view(self):
        request = self.factory.get(reverse("diets:diet-detail", kwargs={"pk": self.diet.pk}))
        response = DietDetailView.as_view()(request, pk=self.diet.pk)
        self.assertEqual(response.status_code, 200)
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
        request = self.factory.post(reverse("diets:diet-create"), data=data)
        response = DietCreateView.as_view()(request)
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
        request = self.factory.post(reverse("diets:diet-update", args=(self.diet.pk,)), data=updated_data)
        response = DietUpdateView.as_view()(request, pk=self.diet.pk)
        self.assertEqual(response.status_code, 302)
        self.diet.refresh_from_db()
        self.assertEqual(self.diet.name, "Updated Diet")
        self.assertEqual(self.diet.description, "Updated Description")
        self.assertEqual(self.diet.caloric_demand, 3200)

    def test_diet_delete_view(self):
        request = self.factory.post(reverse("diets:diet-delete", args=(self.diet.pk,)))
        response = DietDeleteView.as_view()(request, pk=self.diet.pk)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Diet.objects.filter(pk=self.diet.pk).exists())
