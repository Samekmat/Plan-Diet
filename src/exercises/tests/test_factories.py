from django.test import TestCase

from exercises.choices import DIFFICULTIES
from exercises.factories import ExerciseFactory, MuscleGroupFactory, SportTypeFactory
from exercises.models import Exercise, MuscleGroup, SportType


class MuscleGroupFactoryTest(TestCase):
    def test_muscle_group_factory(self):
        muscle_group = MuscleGroupFactory()
        self.assertIsInstance(muscle_group, MuscleGroup)
        self.assertTrue(muscle_group.name)

    def test_bulk_muscle_group_creation(self):
        muscle_groups = MuscleGroupFactory.create_batch(5)
        self.assertEqual(len(muscle_groups), 5)
        for muscle_group in muscle_groups:
            self.assertIsInstance(muscle_group, MuscleGroup)
            self.assertTrue(muscle_group.name)


class SportTypeFactoryTest(TestCase):
    def test_sport_type_factory(self):
        sport_type = SportTypeFactory()
        self.assertIsInstance(sport_type, SportType)
        self.assertTrue(sport_type.name)

    def test_bulk_sport_type_creation(self):
        sport_types = SportTypeFactory.create_batch(5)
        self.assertEqual(len(sport_types), 5)
        for sport_type in sport_types:
            self.assertIsInstance(sport_type, SportType)
            self.assertTrue(sport_type.name)


class TestExerciseFactory(TestCase):
    def setUp(self):
        self.exercise = ExerciseFactory()
        self.muscle = MuscleGroupFactory()
        self.type = SportTypeFactory()

    def test_create_exercise(self):
        self.assertTrue(self.exercise.name)
        self.assertTrue(self.exercise.description)
        self.assertTrue(self.exercise.difficulty)
        self.assertIn(self.exercise.difficulty, [choice[0] for choice in DIFFICULTIES])
        self.assertTrue(self.exercise.category)

    def test_set_muscles_and_types(self):
        self.assertEqual(self.exercise.muscles.count(), 0)
        self.assertEqual(self.exercise.type.count(), 0)

        muscles = [self.muscle]
        exercise_with_muscles = ExerciseFactory()
        exercise_with_muscles.muscles.set(muscles)

        self.assertEqual(exercise_with_muscles.muscles.count(), len(muscles))
        self.assertEqual(exercise_with_muscles.type.count(), 0)

        types = [self.type]
        exercise_with_types = ExerciseFactory()
        exercise_with_types.type.set(types)

        self.assertEqual(exercise_with_types.muscles.count(), 0)
        self.assertEqual(exercise_with_types.type.count(), len(types))

    def test_bulk_exercise_creation(self):
        exercises = ExerciseFactory.create_batch(5)
        self.assertEqual(len(exercises), 5)
        for exercise in exercises:
            self.assertIsInstance(exercise, Exercise)
            self.assertTrue(exercise.name)
