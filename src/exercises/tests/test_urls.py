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

    def test_sporttype_list_url(self):
        url = reverse("exercises:sporttypes")
        self.assertEqual(resolve(url).func.view_class, SportTypeListView)

    def test_sporttype_create_url(self):
        url = reverse("exercises:sporttype-create")
        self.assertEqual(resolve(url).func.view_class, SportTypeCreateView)

    def test_sporttype_update_url(self):
        url = reverse("exercises:sporttype-update", kwargs={"pk": 1})
        self.assertEqual(resolve(url).func.view_class, SportTypeUpdateView)

    def test_sporttype_delete_url(self):
        url = reverse("exercises:sporttype-delete", kwargs={"pk": 1})
        self.assertEqual(resolve(url).func.view_class, SportTypeDeleteView)

    def test_musclegroup_list_url(self):
        url = reverse("exercises:musclegroups")
        self.assertEqual(resolve(url).func.view_class, MuscleGroupListView)

    def test_musclegroup_create_url(self):
        url = reverse("exercises:musclegroup-create")
        self.assertEqual(resolve(url).func.view_class, MuscleGroupCreateView)

    def test_musclegroup_update_url(self):
        url = reverse("exercises:musclegroup-update", kwargs={"pk": 1})
        self.assertEqual(resolve(url).func.view_class, MuscleGroupUpdateView)

    def test_musclegroup_delete_url(self):
        url = reverse("exercises:musclegroup-delete", kwargs={"pk": 1})
        self.assertEqual(resolve(url).func.view_class, MuscleGroupDeleteView)
