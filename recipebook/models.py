from django.db import models
from django.urls import reverse


class Recipe(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True, default='')
    ingredients = models.TextField(blank=True, default='')
    steps = models.TextField(blank=True, default='')
    icon_class = models.CharField(max_length=100)
    accent = models.CharField(max_length=32)
    order = models.PositiveIntegerField(default=0)
    published = models.BooleanField(default=True)

    class Meta:
        ordering = ['order', 'title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('recipe_detail', kwargs={'slug': self.slug})
