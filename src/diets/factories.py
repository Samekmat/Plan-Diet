import factory

from diets.models import Diet


class DietFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Diet

    name = factory.Faker("word")
    caloric_demand = factory.Faker("random_int", min=1000, max=3500)
    carbs_demand = factory.Faker("random_int", min=50, max=250)
    protein_demand = factory.Faker("random_int", min=50, max=300)
    fat_demand = factory.Faker("random_int", min=20, max=150)
    description = factory.Faker("text", max_nb_chars=200)
