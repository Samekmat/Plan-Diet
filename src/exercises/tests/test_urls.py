from django.test import SimpleTestCase
from django.urls import resolve, reverse

from exercises.views.exercise import (
    ExerciseCreateView,
    ExerciseDeleteView,
    ExerciseDetailView,
    ExerciseListView,
    ExerciseUpdateView,
)
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


class ExerciseUrlsTest(SimpleTestCase):
    def test_exercise_detail_url(self):
        url = reverse("exercises:exercise-detail", kwargs={"pk": 1})
        self.assertEqual(resolve(url).func.view_class, ExerciseDetailView)

    def test_exercise_list_url(self):
        url = reverse("exercises:exercises")
        self.assertEqual(resolve(url).func.view_class, ExerciseListView)

    def test_exercise_create_url(self):
        url = reverse("exercises:exercise-create")
        self.assertEqual(resolve(url).func.view_class, ExerciseCreateView)

    def test_exercise_update_url(self):
        url = reverse("exercises:exercise-update", kwargs={"pk": 1})
        self.assertEqual(resolve(url).func.view_class, ExerciseUpdateView)

    def test_exercise_delete_url(self):
        url = reverse("exercises:exercise-delete", kwargs={"pk": 1})
        self.assertEqual(resolve(url).func.view_class, ExerciseDeleteView)

    def test_sport_type_list_url(self):
        url = reverse("exercises:sport-types")
        self.assertEqual(resolve(url).func.view_class, SportTypeListView)

    def test_sport_type_create_url(self):
        url = reverse("exercises:sport-type-create")
        self.assertEqual(resolve(url).func.view_class, SportTypeCreateView)

    def test_sport_type_update_url(self):
        url = reverse("exercises:sport-type-update", kwargs={"pk": 1})
        self.assertEqual(resolve(url).func.view_class, SportTypeUpdateView)

    def test_sport_type_delete_url(self):
        url = reverse("exercises:sport-type-delete", kwargs={"pk": 1})
        self.assertEqual(resolve(url).func.view_class, SportTypeDeleteView)

    def test_muscle_group_list_url(self):
        url = reverse("exercises:muscle-groups")
        self.assertEqual(resolve(url).func.view_class, MuscleGroupListView)

    def test_muscle_group_create_url(self):
        url = reverse("exercises:muscle-group-create")
        self.assertEqual(resolve(url).func.view_class, MuscleGroupCreateView)

    def test_muscle_group_update_url(self):
        url = reverse("exercises:muscle-group-update", kwargs={"pk": 1})
        self.assertEqual(resolve(url).func.view_class, MuscleGroupUpdateView)

    def test_muscle_group_delete_url(self):
        url = reverse("exercises:muscle-group-delete", kwargs={"pk": 1})
        self.assertEqual(resolve(url).func.view_class, MuscleGroupDeleteView)
