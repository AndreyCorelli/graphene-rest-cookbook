import graphene
from django.db.models import Q

from cookbook.ingredients.models import Category, Ingredient, Dish
from cookbook.schema_types import IngredientType, DishType, CategoryType


class Query(graphene.ObjectType):
    all_ingredients = graphene.List(IngredientType)
    all_dishes = graphene.List(DishType,
                               search=graphene.String(),
                               first=graphene.Int(),
                               skip=graphene.Int())
    category_by_name = graphene.Field(CategoryType, name=graphene.String(required=True))

    def resolve_all_dishes(root, info, search=None, first=None, skip=None, **kwargs):
        qs = Dish.objects.prefetch_related('ingredients').all()

        if search:
            filter = (
                    Q(name__icontains=search) |
                    Q(recipe__icontains=search)
            )
            qs = qs.filter(filter)

        if skip:
            qs = qs[skip:]

        if first:
            qs = qs[:first]

        return qs

    def resolve_all_ingredients(root, info):
        return Ingredient.objects.select_related("category").all()

    def resolve_category_by_name(root, info, name):
        try:
            return Category.objects.get(name=name)
        except Category.DoesNotExist:
            return None
