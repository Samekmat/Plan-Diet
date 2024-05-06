from http import HTTPStatus

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from users.factories import CustomUserFactory

User = get_user_model()


class ProfileViewTestCase(TestCase):
    def setUp(self):
        self.user = CustomUserFactory()

    def test_profile_view(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("users:profile"))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, "users/profile.html")
        self.assertEqual(response.context["current_user"], self.user)


class RegisterViewTestCase(TestCase):
    def setUp(self):
        self.existing_user = CustomUserFactory(
            username="existing_user",
            email="existing_user@example.com",
        )

    def test_register_view_valid_data(self):
        data = {
            "username": "test_user",
            "email": "test_user@gmail.com",
            "password1": "qhweduqwnyduqwhnc",
            "password2": "qhweduqwnyduqwhnc",
            "age": 25,
            "height": 176,
            "weight": 90,
            "sex": "male",
        }
        response = self.client.post(reverse("users:register"), data=data)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertTrue(User.objects.filter(username="test_user").exists())
        self.assertRedirects(response, reverse("users:login"))

    def test_register_view_different_password(self):
        data = {
            "username": "test_user",
            "password1": "password123",
            "password2": "password_wrong",
        }
        response = self.client.post(reverse("users:register"), data)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        form = response.context["form"]
        self.assertTrue(form.has_error("password2", "password_mismatch"))

    def test_register_view_user_with_provided_username_already_exists(self):
        data = {
            "username": "existing_user",
            "password1": "existing_password",
            "password2": "existing_password",
        }
        response = self.client.post(reverse("users:register"), data)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        form = response.context["form"]
        self.assertTrue(form.has_error("username", "unique"))

    def test_register_view_user_password_is_too_common(self):
        common_password = "password123"
        data = {
            "username": "test_user",
            "password1": common_password,
            "password2": common_password,
        }
        response = self.client.post(reverse("users:register"), data)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        form = response.context["form"]
        self.assertTrue(form.has_error("password2", "password_too_common"))

    def test_register_view_user_with_invalid_age(self):
        data = {
            "username": "test_user",
            "email": "test_user@gmail.com",
            "password1": "ZAQ!2wsx",
            "password2": "ZAQ!2wsx",
            "age": -10,  # Invalid age
            "height": 180,
            "weight": 70,
            "sex": "male",
        }
        response = self.client.post(reverse("users:register"), data)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        form = response.context["form"]
        self.assertTrue(form.has_error("age", "min_value"))  # Check if the age error is triggered

    def test_register_view_user_with_invalid_height(self):
        data = {
            "username": "test_user",
            "email": "test_user@gmail.com",
            "password1": "ZAQ!2wsx",
            "password2": "ZAQ!2wsx",
            "age": 25,
            "height": -180,
            "weight": 70,
            "sex": "male",
        }
        response = self.client.post(reverse("users:register"), data)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        form = response.context["form"]
        self.assertTrue(form.has_error("height", "min_value"))

    def test_register_view_user_with_invalid_weight(self):
        data = {
            "username": "test_user",
            "email": "test_user@gmail.com",
            "password1": "ZAQ!2wsx",
            "password2": "ZAQ!2wsx",
            "age": 20,
            "height": 180,
            "weight": -70,
            "sex": "male",
        }
        response = self.client.post(reverse("users:register"), data)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        form = response.context["form"]
        self.assertTrue(form.has_error("weight", "min_value"))
