from django.contrib.auth import get_user_model
from django.test import TestCase

from users.factories import CustomUserFactory

CustomUser = get_user_model()


class CustomUserFactoryTest(TestCase):
    def test_bulk_create_custom_users(self):
        custom_users = CustomUserFactory.create_batch(5)

        all_custom_users = CustomUser.objects.all()

        self.assertEqual(all_custom_users.count(), len(custom_users))

        for user in all_custom_users:
            self.assertIsInstance(user, CustomUser)

        for user in all_custom_users:
            self.assertTrue(user.username)
            self.assertTrue(user.age)
            self.assertTrue(user.height)
            self.assertTrue(user.weight)
            self.assertTrue(user.sex)
            self.assertTrue(user.plan)
            self.assertTrue(user.diet)
