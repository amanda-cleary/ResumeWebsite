from django.db import migrations


def seed_recipes(apps, schema_editor):
    Recipe = apps.get_model('recipebook', 'Recipe')
    recipes = [
        {
            'title': 'Pancake Cookies',
            'slug': 'pancake-cookies',
            'page_url': 'recipes/pancakecookies.html',
            'icon_class': 'fa-solid fa-stroopwafel',
            'accent': '#846b77',
            'order': 1,
        },
        {
            'title': 'Cake Cookies',
            'slug': 'cake-cookies',
            'page_url': 'recipes/cakecookies.html',
            'icon_class': 'fa-solid fa-cookie',
            'accent': '#8f4c6c',
            'order': 2,
        },
        {
            'title': 'Peach Croissant Dumplings',
            'slug': 'peach-croissant-dumplings',
            'page_url': 'recipes/peachdumplings.html',
            'icon_class': 'fa-solid fa-apple-alt',
            'accent': '#bc7c95',
            'order': 3,
        },
    ]

    for recipe in recipes:
        Recipe.objects.update_or_create(slug=recipe['slug'], defaults=recipe)


def unseed_recipes(apps, schema_editor):
    Recipe = apps.get_model('recipebook', 'Recipe')
    Recipe.objects.filter(slug__in=[
        'pancake-cookies',
        'cake-cookies',
        'peach-croissant-dumplings',
    ]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('recipebook', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_recipes, unseed_recipes),
    ]
