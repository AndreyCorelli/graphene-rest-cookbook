from typing import Optional
import graphene
from cookbook.ingredients.models import Dish, Ingredient
from cookbook.schema_types import DishType


class DishInput(graphene.InputObjectType):
    name = graphene.String(description='Name of your dish')
    recipe = graphene.String(description='Recipe of your dish')
    complexity = graphene.Int(description='Complexity of your dish')
    ingredients = graphene.List(graphene.Int, description='List of ingredients (ids)')


class DishUpdateInput(DishInput):
    id = graphene.Int()


class CreateDish(graphene.Mutation):
    dish = graphene.Field(DishType)
    ok = graphene.Boolean()

    class Arguments:
        dish_data = DishInput(required=True)

    @staticmethod
    def mutate(root, info, dish_data: Optional[DishInput] = None):
        # if not info.context.user.is_authenticated:
        #    return CreateDish(errors=json.dumps('Please Login to create new records'))
        dish = Dish.objects.create(
            name=dish_data.name,
            recipe=dish_data.recipe,
            complexity=dish_data.complexity)
        for ig_id in dish_data.ingredients:
            dish.ingredients.add(Ingredient.objects.get(pk=ig_id))
        dish.save()
        return CreateDish(dish=dish, ok=True)


class UpdateDish(graphene.Mutation):
    dish = graphene.Field(DishType)
    ok = graphene.Boolean()

    class Arguments:
        dish_data = DishUpdateInput(required=True)

    @staticmethod
    def mutate(root, info, dish_data: Optional[DishUpdateInput] = None):
        # if not info.context.user.is_authenticated:
        #    return CreateDish(errors=json.dumps('Please Login to create new records'))
        dish = Dish.objects.get(pk=dish_data.id)
        if not dish:
            raise RuntimeError(f'Dish with ID={dish_data.id} was not found')

        if dish_data.name:
            dish.name = dish_data.name
        if dish_data.recipe:
            dish.recipe = dish_data.recipe
        if dish_data.complexity:
            dish.complexity = dish_data.complexity

        if dish_data.ingredients is not None:
            dish.ingredients.clear()
            for ig_id in dish_data.ingredients:
                dish.ingredients.add(Ingredient.objects.get(pk=ig_id))
        dish.save()
        return UpdateDish(dish=dish, ok=True)


class DeleteDish(graphene.Mutation):
    ok = graphene.Boolean()

    class Arguments:
        id = graphene.ID()

    @classmethod
    def mutate(cls, root, info, **kwargs):
        # if not info.context.user.is_authenticated:
        #    return DeleteDish(errors=json.dumps('Please Login to delete records'))
        obj = Dish.objects.get(pk=kwargs["id"])
        obj.delete()
        return cls(ok=True)


class Mutation(graphene.ObjectType):
    create_dish = CreateDish.Field()
    update_dish = UpdateDish.Field()
    delete_dish = DeleteDish.Field()
