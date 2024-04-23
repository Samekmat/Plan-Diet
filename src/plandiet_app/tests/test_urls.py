from django.test import SimpleTestCase
from django.urls import reverse


class UrlsTest(SimpleTestCase):
    def test_index_url(self):
        url = reverse("index")
        self.assertEqual(url, "/")

    def test_macro_calculator_url(self):
        url = reverse("macro-calc")
        self.assertEqual(url, "/macro_calculator/")
