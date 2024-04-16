from django.test import SimpleTestCase
from django.urls import resolve, reverse

from categories.views import (
    CategoryCreateView,
    CategoryDeleteView,
    CategoryListView,
    CategoryView,
)


class CategoryUrlsTest(SimpleTestCase):
    def test_category_list_url_resolves(self):
        url = reverse("categories:categories")
        self.assertEqual(resolve(url).func.view_class, CategoryListView)

    def test_category_detail_url_resolves(self):
        url = reverse("categories:category-detail", args=[1])
        self.assertEqual(resolve(url).func.view_class, CategoryView)

    def test_category_delete_url_resolves(self):
        url = reverse("categories:category-delete", args=[1])
        self.assertEqual(resolve(url).func.view_class, CategoryDeleteView)

    def test_category_create_url_resolves(self):
        url = reverse("categories:category-create")
        self.assertEqual(resolve(url).func.view_class, CategoryCreateView)
