from django.test import TestCase

from users.forms import CustomUserCreationForm


class RegistrationFormTest(TestCase):
    def test_registration_form_valid_data(self):
        form_data = {
            "username": "testuser",
            "password1": "testpassword123",
            "password2": "testpassword123",
            "first_name": "John",
            "last_name": "Doe",
            "email": "test@example.com",
            "age": 25,
            "height": 180,
            "weight": 75.5,
            "sex": "male",
        }
        form = CustomUserCreationForm(data=form_data)
        self.assertTrue(form.is_valid(), form.errors)

    def test_registration_form_passwords_not_matching(self):
        form_data = {
            "username": "testuser",
            "password1": "testpassword123",
            "password2": "differentpassword",
            "first_name": "John",
            "last_name": "Doe",
            "email": "test@example.com",
            "age": 25,
            "height": 180,
            "weight": 75.5,
            "sex": "male",
        }
        form = CustomUserCreationForm(data=form_data)
        self.assertFalse(form.is_valid())
