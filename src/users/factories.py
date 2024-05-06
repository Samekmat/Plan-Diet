import factory
from django.contrib.auth import get_user_model

from diets.factories import DietFactory
from plans.factories import PlanFactory

CustomUser = get_user_model()


class CustomUserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CustomUser

    username = factory.Faker("user_name")
    age = factory.Faker("random_int", min=1, max=100)
    height = factory.Faker("random_int", min=20, max=220)
    weight = factory.Faker("random_int", min=5, max=180)
    sex = factory.Faker("random_element", elements=["male", "female"])
    plan = factory.SubFactory(PlanFactory)
    diet = factory.SubFactory(DietFactory)
