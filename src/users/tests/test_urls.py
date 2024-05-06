from django.test import Client, TestCase
from django.urls import reverse

from users.factories import CustomUserFactory


class UserViewsTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_login_view(self):
        response = self.client.get(reverse("users:login"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/login.html")

    def test_register_view(self):
        response = self.client.get(reverse("users:register"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/register.html")

    def test_logout_view(self):
        response = self.client.post(reverse("users:logout"))
        self.assertEqual(response.status_code, 302)

    def test_profile_view(self):
        custom_user = CustomUserFactory()

        self.client.force_login(custom_user)

        response = self.client.get(reverse("users:profile"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/profile.html")
