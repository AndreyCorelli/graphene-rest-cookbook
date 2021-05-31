from cookbook.api.annotations import model_exception_handler
from cookbook.ingredients.api.schemas import CategorySchema
from cookbook.ingredients.models import Category


class ProductService:
    @model_exception_handler()
    def create_category(self, category_schema: CategorySchema):
        cat = Category(name=category_schema.name)
        cat.full_clean(validate_unique=True)
        cat.save()
        return cat
