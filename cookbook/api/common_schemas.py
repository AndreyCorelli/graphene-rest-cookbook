from typing import List

from ninja import Schema


class ModelErrorSchema(Schema):
    message: str


class FieldErrorSchema(ModelErrorSchema):
    field: str


class ValidationErrorSchema(ModelErrorSchema):
    errors: List[FieldErrorSchema]
