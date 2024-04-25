import factory

from plans.models import Plan


class PlanFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Plan

    name = factory.Faker("sentence", nb_words=4)
    diet = factory.SubFactory("diets.factories.DietFactory")

    @factory.post_generation
    def set_exercises(self, create, extracted, **kwargs):
        if extracted:
            self.exercises.set(extracted)
