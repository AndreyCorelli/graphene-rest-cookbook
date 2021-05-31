import inspect

from django.core.exceptions import ValidationError

from cookbook.api.common_schemas import ValidationErrorSchema, FieldErrorSchema


def model_exception_handler():
    def wrapper(func):
        def decorator(*args, **kwargs):
            try:
                if inspect.ismethod(func):
                    if len(args) <= 1:
                        res = func(**kwargs)
                    else:
                        res = func(args[1:], **kwargs)
                else:
                    res = func(*args, **kwargs)
            except ValidationError as e:
                error = ValidationErrorSchema(message='There are errors', field='', errors=[])
                for field_name in e.error_dict:
                    er = e.error_dict[field_name]
                    error.errors.append(FieldErrorSchema(field=field_name, message=f'{er}'))
                return error
            return res

        decorator._original = func
        return decorator
    return wrapper
