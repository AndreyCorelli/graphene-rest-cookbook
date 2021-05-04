import graphene
from graphene_django import DjangoObjectType

from cookbook.ingredients.models import Category, Ingredient, Dish


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ('id', 'name', 'ingredients')


class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient
        fields = ('id', 'name', 'notes', 'category')


class DishType(DjangoObjectType):
    class Meta:
        model = Dish
        fields = ('id', 'recipe', 'complexity', 'ingredients')
        ingredients = graphene.List(IngredientType)

        @graphene.resolve_only_args
        def resolve_ingredients(self):
            return self.ingredients.all()