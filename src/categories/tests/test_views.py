from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from categories.factories import CategoryFactory


class CategoryViewsTest(TestCase):
    def setUp(self):
        self.category = CategoryFactory()
        self.expected_redirect_url = reverse("categories:categories")

    def test_category_list_view(self):
        response = self.client.get(reverse("categories:categories"))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertIn(self.category, response.context_data["categories"])

    def test_category_detail_view(self):
        response = self.client.get(reverse("categories:category-detail", kwargs={"pk": self.category.pk}))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data["category"], self.category)

    def test_category_create_view(self):
        form_data = {"name": self.category.name, "description": self.category.description}
        response = self.client.post(reverse("categories:category-create"), data=form_data)

        self.assertRedirects(response, self.expected_redirect_url)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

    def test_category_update_view(self):
        form_data = {"name": "Updated category", "description": "This is an updated category."}
        response = self.client.post(
            reverse("categories:category-update", kwargs={"pk": self.category.pk}), data=form_data
        )

        self.assertRedirects(response, self.expected_redirect_url)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

    def test_category_delete_view(self):
        response = self.client.post(reverse("categories:category-delete", kwargs={"pk": self.category.pk}))
        self.assertRedirects(response, self.expected_redirect_url)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
