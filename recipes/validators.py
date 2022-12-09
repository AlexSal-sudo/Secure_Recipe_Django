from django.core.validators import BaseValidator
from django.core.exceptions import ValidationError
import jsonschema


def check_not_none_and_unique_ingredients(list_of_ingredients: list):
    if not isinstance(list_of_ingredients, list):
        raise ValidationError("Please, fill the ingredients properly")
    print("QUI")
    for i in range(len(list_of_ingredients)):
        for j in range(len(list_of_ingredients)):
            if i != j and list_of_ingredients[i]['name'] == list_of_ingredients[j]['name']:
                raise ValidationError(
                    f"There are some redundant ingredients! <{list_of_ingredients[i]['name'].upper()}>")


class JSONSchemaValidator(BaseValidator):
    def compare(self, value: list, schema):
        try:
            jsonschema.validate(value, schema)
        except jsonschema.exceptions.ValidationError as e:
            raise ValidationError(e.message)
