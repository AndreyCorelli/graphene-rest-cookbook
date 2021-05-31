from cookbook.ingredients.api.ProductService import ProductService
from cookbook.ingredients.api.schemas import CategorySchema
from ninja import Router


router = Router()

product_service = ProductService()


@router.post("/categories", auth=None)
def create_category(_request, category: CategorySchema):
    return product_service.create_category(category)
