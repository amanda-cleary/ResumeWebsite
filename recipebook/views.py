from django.shortcuts import get_object_or_404, redirect, render
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required
from django.conf import settings

from .forms import RecipeForm
from .models import Recipe


def render_page(request, template_name, active_page, asset_prefix='', extra_context=None):
    context = {
        'active_page': active_page,
        'asset_prefix': asset_prefix,
    }
    if extra_context:
        context.update(extra_context)
    return render(request, template_name, context)


def home(request):
    recipes = Recipe.objects.all()
    return render_page(
        request,
        'index.html',
        active_page='about',
        extra_context={'recipes': recipes},
    )


def experiences(request):
    return render_page(request, 'experiences.html', active_page='experiences')


def portfolio(request):
    return render_page(request, 'portfolio.html', active_page='portfolio')


def recipes_index(request):
    recipes = Recipe.objects.all()
    return render_page(
        request,
        'recipebook/recipes.html',
        active_page='about',
        extra_context={
            'recipes': recipes,
            'recipe_submission_form_url': settings.RECIPE_SUBMISSION_FORM_URL,
        },
    )


def recipe_detail(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    ingredients = [line.strip() for line in recipe.ingredients.splitlines() if line.strip()]
    steps = [line.strip() for line in recipe.steps.splitlines() if line.strip()]
    return render_page(
        request,
        'recipebook/recipe.html',
        active_page='about',
        asset_prefix='../',
        extra_context={
            'recipe': recipe,
            'recipe_ingredients': ingredients,
            'recipe_steps': steps,
        },
    )


@login_required
def edit_recipe(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    cancel_url = recipe.get_absolute_url()

    icon_choices = [
        "fa-solid fa-cookie",
        "fa-solid fa-apple-whole",
        "fa-solid fa-carrot",
        "fa-solid fa-bread-slice",
        "fa-solid fa-ice-cream",
        "fa-solid fa-pepper-hot",
        "fa-solid fa-bowl-food",
        "fa-solid fa-cake-candles",
        "fa-solid fa-mug-hot",
        "fa-solid fa-burger",
        "fa-solid fa-fish",
        "fa-solid fa-pizza-slice",
        "fa-solid fa-blender",
        "fa-solid fa-egg",
        "fa-solid fa-candy-cane",
        "fa-solid fa-seedling",
        "fa-solid fa-drumstick-bite",
        "fa-solid fa-cheese",
    ]

    color_choices = [
        ("var(--color-recipe-var1)", "var(--color-recipe-var1-dark)"),
        ("var(--color-recipe-var2)", "var(--color-recipe-var2-dark)"),
        ("var(--color-recipe-var3)", "var(--color-recipe-var3-dark)"),
        ("var(--color-recipe-var4)", "var(--color-recipe-var4-dark)"),
    ]

    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            updated_recipe = form.save(commit=False)
            updated_recipe.slug = build_unique_slug(updated_recipe.title, instance=recipe)
            updated_recipe.save()
            return redirect(updated_recipe.get_absolute_url())
    else:
        form = RecipeForm(instance=recipe)

    return render_page(
        request,
        'recipebook/edit_recipe.html',
        active_page='about',
        asset_prefix='../',
        extra_context={
            'recipe': recipe,
            'form': form,
            'cancel_url': cancel_url,
            'icon_choices': icon_choices,      
            'color_choices': color_choices,    
        },
    )



@login_required
def delete_recipe(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)

    if request.method != 'POST':
        return redirect('recipes')

    recipe.delete()
    return redirect('recipes')


def legacy_recipe_redirect(request, slug):
    return redirect('recipe_detail', slug=slug)


def build_unique_slug(title, instance=None):
    base_slug = slugify(title)
    if not base_slug:
        return ''

    slug = base_slug
    suffix = 2
    queryset = Recipe.objects.all()
    if instance and instance.pk:
        queryset = queryset.exclude(pk=instance.pk)

    while queryset.filter(slug=slug).exists():
        slug = f'{base_slug}-{suffix}'
        suffix += 1

    return slug


@login_required
def create_recipe(request):
    if request.method != 'POST':
        return redirect('recipes')

    form = RecipeForm(request.POST)
    if not form.is_valid():
        return redirect('recipes')

    recipe = form.save(commit=False)
    recipe.slug = build_unique_slug(recipe.title)
    if not recipe.slug:
        return redirect('recipes')

    recipe.save()

    return redirect('recipes')
