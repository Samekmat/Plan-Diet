from django.test import RequestFactory, TestCase
from django.urls import reverse

from categories.factories import CategoryFactory
from categories.views import (
    CategoryCreateView,
    CategoryDeleteView,
    CategoryDetailView,
    CategoryListView,
    CategoryUpdateView,
)


class CategoryViewsTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.category = CategoryFactory()

    def test_category_list_view(self):
        request = self.factory.get(reverse("categories:categories"))
        response = CategoryListView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.category, response.context_data["categories"])

    def test_category_detail_view(self):
        request = self.factory.get(reverse("categories:category-detail", kwargs={"pk": self.category.pk}))
        response = CategoryDetailView.as_view()(request, pk=self.category.pk)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context_data["category"], self.category)

    def test_category_create_view(self):
        form_data = {"name": self.category.name, "description": self.category.description}
        request = self.factory.post(reverse("categories:category-create"), data=form_data)
        response = CategoryCreateView.as_view()(request)
        self.assertEqual(response.status_code, 302)

    def test_category_update_view(self):
        form_data = {"name": "Updated category", "description": "This is an updated category."}
        request = self.factory.post(
            reverse("categories:category-update", kwargs={"pk": self.category.pk}), data=form_data
        )
        response = CategoryUpdateView.as_view()(request, pk=self.category.pk)
        self.assertEqual(response.status_code, 302)

    def test_category_delete_view(self):
        request = self.factory.post(reverse("categories:category-delete", kwargs={"pk": self.category.pk}))
        response = CategoryDeleteView.as_view()(request, pk=self.category.pk)
        self.assertEqual(response.status_code, 302)
