from django.test import SimpleTestCase
from django.urls import resolve, reverse

from diets.views import (
    DietCreateView,
    DietDeleteView,
    DietDetailView,
    DietListView,
    DietUpdateView,
)


class TestUrls(SimpleTestCase):
    def test_diet_list_url_resolves(self):
        url = reverse("diets:diet-list")
        self.assertEqual(resolve(url).func.view_class, DietListView)

    def test_diet_detail_url_resolves(self):
        url = reverse("diets:diet-detail", args=[1])
        self.assertEqual(resolve(url).func.view_class, DietDetailView)

    def test_diet_create_url_resolves(self):
        url = reverse("diets:diet-create")
        self.assertEqual(resolve(url).func.view_class, DietCreateView)

    def test_diet_update_url_resolves(self):
        url = reverse("diets:diet-update", args=[1])
        self.assertEqual(resolve(url).func.view_class, DietUpdateView)

    def test_diet_delete_url_resolves(self):
        url = reverse("diets:diet-delete", args=[1])
        self.assertEqual(resolve(url).func.view_class, DietDeleteView)
