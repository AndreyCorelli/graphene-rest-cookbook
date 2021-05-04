from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    notes = models.TextField()
    category = models.ForeignKey(
        Category, related_name="ingredients", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=100)
    recipe = models.TextField()
    ingredients = models.ManyToManyField(Ingredient)
    complexity = models.IntegerField(default=5)

    def __str__(self):
        return self.name
