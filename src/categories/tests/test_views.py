from django.test import TestCase
from django.urls import reverse

from categories.forms import CategoryForm
from categories.models import Category


class CategoryViewsTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Test")

    def tearDown(self):
        self.category.delete()
        Category.objects.filter(name="New Category").delete()

    def test_category_list_view(self):
        response = self.client.get(reverse("categories:categories"))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context["categories"], [self.category])

    def test_category_detail_view(self):
        response = self.client.get(reverse("categories:category-detail", args=(self.category.pk,)))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["category"], self.category)

    def test_category_create_view_get(self):
        response = self.client.get(reverse("categories:category-create"))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context["form"], CategoryForm)

    def test_category_create_view_post(self):
        data = {"name": "New Category", "description": "New Description"}
        response = self.client.post(reverse("categories:category-create"), data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Category.objects.filter(name="New Category", description="New Description").exists())

    def test_category_delete_view_get(self):
        response = self.client.get(reverse("categories:category-delete", args=[self.category.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["category"], self.category)

    def test_category_delete_view_post(self):
        response = self.client.post(reverse("categories:category-delete", args=[self.category.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Category.objects.filter(pk=self.category.pk).exists())
