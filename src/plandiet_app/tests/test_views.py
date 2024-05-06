from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from users.models import CustomUser as User


class MacroCalculatorViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.client.login(username="testuser", password="12345")
        self.url = reverse("macro-calc")

    def test_get_with_authenticated_user(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, "plandiet_app/macrocalculator.html")

    def test_get_with_unauthenticated_user(self):
        self.client.logout()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_post_with_valid_data(self):
        data = {"age": 30, "height": 175, "weight": 70, "sex": "male", "activity": 1.55, "goal": "maintain"}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, "plandiet_app/macrocalculator.html")
        self.assertIn("bmr", response.context)
        self.assertIn("cpm", response.context)

    def test_post_with_invalid_data(self):
        data = {"age": "abc", "height": -175, "weight": "xyz", "sex": "unknown", "activity": "high", "goal": "unknown"}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        form = response.context["form"]
        self.assertTrue(form.errors)
        self.assertIn("age", form.errors)
        self.assertIn("height", form.errors)
        self.assertIn("weight", form.errors)
        self.assertIn("sex", form.errors)
        self.assertIn("activity", form.errors)
        self.assertIn("goal", form.errors)

        self.assertEqual(form.errors["age"], ["Enter a whole number."])
        self.assertEqual(form.errors["height"], ["Height must be a positive number."])
        self.assertEqual(form.errors["weight"], ["Enter a number."])
        self.assertEqual(form.errors["sex"], ["Select a valid choice. unknown is not one of the available choices."])
        self.assertEqual(
            form.errors["activity"],
            [f"Select a valid choice. {data['activity']} is not one of the available choices."],
        )
        self.assertEqual(form.errors["goal"], ["Select a valid choice. unknown is not one of the available choices."])

    def test_post_with_authenticated_user(self):
        self.client.logout()
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
