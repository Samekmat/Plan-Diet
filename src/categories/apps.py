from django.apps import AppConfig

from categories.choices import CATEGORIES


class CategoriesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "categories"

    def ready(self):
        from .models import Category

        existing_categories = Category.objects.all()
        existing_names = set(category.name for category in existing_categories)
        for category_key, category_name in CATEGORIES:
            if category_name not in existing_names:
                Category.objects.create(name=category_name, description=category_key)
