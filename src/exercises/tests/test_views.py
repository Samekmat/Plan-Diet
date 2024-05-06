from django.test import TestCase
from django.test.client import Client, RequestFactory
from django.urls import reverse, reverse_lazy

from categories.factories import CategoryFactory
from exercises.factories import ExerciseFactory, MuscleGroupFactory, SportTypeFactory
from exercises.models import Exercise, MuscleGroup, SportType
from exercises.views.muscle_group import (
    MuscleGroupCreateView,
    MuscleGroupDeleteView,
    MuscleGroupListView,
    MuscleGroupUpdateView,
)
from exercises.views.sport_type import (
    SportTypeCreateView,
    SportTypeDeleteView,
    SportTypeListView,
    SportTypeUpdateView,
)


class ExerciseViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.muscle = MuscleGroupFactory()
        self.type = SportTypeFactory()
        self.exercise = ExerciseFactory()
        self.category = CategoryFactory()
        self.test_data = {
            "name": "Test Exercise",
            "description": "Test Description",
            "difficulty": "beginner",
            "category": self.category.pk,
            "muscles": [self.muscle.pk],
            "type": [self.type.pk],
        }

    def test_exercise_detail_view(self):
        url = reverse("exercises:exercise-detail", kwargs={"pk": self.exercise.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "exercises/exercise_detail.html")
        self.assertEqual(response.context["exercise"], self.exercise)

    def test_exercise_list_view(self):
        url = reverse("exercises:exercises")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "exercises/exercise_list.html")
        self.assertTrue("exercises" in response.context)
        self.assertTrue(len(response.context["exercises"]) > 0)

    def test_exercise_create_view(self):
        url = reverse("exercises:exercise-create")
        response = self.client.post(url, data=self.test_data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Exercise.objects.filter(name=self.test_data["name"]).exists())

    def test_exercise_update_view(self):
        url = reverse("exercises:exercise-update", kwargs={"pk": self.exercise.pk})
        updated_name = "Updated Test Exercise"
        updated_data = {**self.test_data, "name": updated_name}
        response = self.client.post(url, data=updated_data)
        self.assertEqual(response.status_code, 302)
        self.exercise.refresh_from_db()
        self.assertEqual(self.exercise.name, updated_name)

    def test_exercise_delete_view(self):
        url = reverse("exercises:exercise-delete", kwargs={"pk": self.exercise.pk})
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Exercise.objects.filter(pk=self.exercise.pk).exists())


class MuscleGroupViewsTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.muscle_group = MuscleGroupFactory()
        self.test_data = {
            "name": "Test Muscle Group",
        }

    def test_muscle_group_list_view(self):
        request = self.factory.get(reverse("exercises:muscle-groups"))
        response = MuscleGroupListView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertTrue("muscle_groups" in response.context_data)
        self.assertTrue(len(response.context_data["muscle_groups"]) > 0)

    def test_muscle_group_create_view(self):
        request = self.factory.post(reverse("exercises:muscle-group-create"), data=self.test_data)
        response = MuscleGroupCreateView.as_view()(request)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(MuscleGroup.objects.filter(name=self.test_data["name"]).exists())

    def test_muscle_group_update_view(self):
        updated_name = "Updated Test Muscle Group"
        updated_data = self.test_data.copy()
        updated_data["name"] = updated_name
        request = self.factory.post(
            reverse("exercises:muscle-group-update", kwargs={"pk": self.muscle_group.pk}), data=updated_data
        )
        response = MuscleGroupUpdateView.as_view()(request, pk=self.muscle_group.pk)
        self.assertEqual(response.status_code, 302)
        self.muscle_group.refresh_from_db()
        self.assertEqual(self.muscle_group.name, updated_name)

    def test_muscle_group_delete_view(self):
        request = self.factory.post(reverse("exercises:muscle-group-delete", kwargs={"pk": self.muscle_group.pk}))
        response = MuscleGroupDeleteView.as_view()(request, pk=self.muscle_group.pk)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(MuscleGroup.objects.filter(pk=self.muscle_group.pk).exists())


class SportTypeViewsTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.sport_type = SportTypeFactory()
        self.test_data = {
            "name": "Test Sport Type",
        }

    def test_sport_type_list_view(self):
        url = reverse_lazy("exercises:sport-types")
        request = self.factory.get(url)
        response = SportTypeListView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertTrue("sport_types" in response.context_data)
        self.assertTrue(len(response.context_data["sport_types"]) > 0)

    def test_sport_type_create_view(self):
        url = reverse_lazy("exercises:sport-type-create")
        request = self.factory.post(url, data=self.test_data)
        response = SportTypeCreateView.as_view()(request)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(SportType.objects.filter(name=self.test_data["name"]).exists())

    def test_sport_type_update_view(self):
        url = reverse_lazy("exercises:sport-type-update", kwargs={"pk": self.sport_type.pk})
        updated_name = "Updated Test Sport Type"
        updated_data = self.test_data.copy()
        updated_data["name"] = updated_name
        request = self.factory.post(url, data=updated_data)
        response = SportTypeUpdateView.as_view()(request, pk=self.sport_type.pk)
        self.assertEqual(response.status_code, 302)
        self.sport_type.refresh_from_db()
        self.assertEqual(self.sport_type.name, updated_name)

    def test_sport_type_delete_view(self):
        url = reverse_lazy("exercises:sport-type-delete", kwargs={"pk": self.sport_type.pk})
        request = self.factory.post(url)
        response = SportTypeDeleteView.as_view()(request, pk=self.sport_type.pk)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(SportType.objects.filter(pk=self.sport_type.pk).exists())
