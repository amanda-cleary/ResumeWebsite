from pathlib import Path

from django.urls import path
from django.views.static import serve

from recipebook import views


BASE_DIR = Path(__file__).resolve().parent.parent


urlpatterns = [
    path('', views.home, name='home'),
    path('index.html', views.home, name='index'),
    path('experiences.html', views.experiences, name='experiences'),
    path('portfolio.html', views.portfolio, name='portfolio'),
    path('recipes/create/', views.create_recipe, name='create_recipe'),
    path('recipes/<slug:slug>/', views.recipe_detail, name='recipe_detail'),
    path('recipes/<slug:slug>/edit/', views.edit_recipe, name='edit_recipe'),
    path('recipes/<slug:slug>/delete/', views.delete_recipe, name='delete_recipe'),
    path('recipes/pancakecookies.html', views.legacy_recipe_redirect, {'slug': 'pancake-cookies'}, name='pancakecookies'),
    path('recipes/cakecookies.html', views.legacy_recipe_redirect, {'slug': 'cake-cookies'}, name='cakecookies'),
    path('recipes/peachdumplings.html', views.legacy_recipe_redirect, {'slug': 'peach-croissant-dumplings'}, name='peachdumplings'),
    path('styles.css', serve, {'path': 'styles.css', 'document_root': BASE_DIR}),
    path('styles/<path:path>', serve, {'document_root': BASE_DIR / 'styles'}),
    path('scripts/<path:path>', serve, {'document_root': BASE_DIR / 'scripts'}),
    path('images/<path:path>', serve, {'document_root': BASE_DIR / 'images'}),
    path('files/<path:path>', serve, {'document_root': BASE_DIR / 'files'}),
]
