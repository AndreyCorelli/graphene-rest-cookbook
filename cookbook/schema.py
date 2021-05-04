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


class Query(graphene.ObjectType):
    all_ingredients = graphene.List(IngredientType)
    all_dishes = graphene.List(DishType)
    category_by_name = graphene.Field(CategoryType, name=graphene.String(required=True))

    def resolve_all_dishes(root, info):
        return Dish.objects.prefetch_related('ingredients').all()

    def resolve_all_ingredients(root, info):
        return Ingredient.objects.select_related("category").all()

    def resolve_category_by_name(root, info, name):
        try:
            return Category.objects.get(name=name)
        except Category.DoesNotExist:
            return None


schema = graphene.Schema(query=Query)
