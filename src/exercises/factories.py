import factory

from categories.factories import CategoryFactory
from exercises.choices import DIFFICULTIES
from exercises.models import Exercise, MuscleGroup, SportType


class MuscleGroupFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = MuscleGroup

    name = factory.Faker("word")


class SportTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = SportType

    name = factory.Faker("word")


class ExerciseFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Exercise

    name = factory.Faker("sentence", nb_words=4)
    description = factory.Faker("paragraph")
    difficulty = factory.Iterator([choice[0] for choice in DIFFICULTIES])
    category = factory.SubFactory(CategoryFactory)

    @factory.post_generation
    def set_muscles_and_types(self, create, extracted, **kwargs):
        if extracted:
            for muscle in extracted:
                self.muscles.add(muscle)

        for t in kwargs.get("type", []):
            self.type.add(t)
