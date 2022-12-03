# Generated by Django 4.1.3 on 2022-12-03 10:43

import django.core.validators
from django.db import migrations, models
import recipes.validators


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_alter_recipe_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='description',
            field=models.TextField(max_length=500, validators=[django.core.validators.MaxLengthValidator(limit_value=500), django.core.validators.RegexValidator(regex="^[a-zA-Z0-9À-ú \\'!;\\.,\\n]+$")]),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.JSONField(default=list, validators=[recipes.validators.JSONSchemaValidator(limit_value={'description': 'The ingredients list', 'items': {'maxProperties': 3, 'properties': {'name': {'description': 'The name of the ingredient', 'maxLength': 30, 'minLength': 1, 'pattern': '^[a-zA-ZÀ-ú ]+$', 'type': 'string'}, 'quantity': {'description': 'The quantity of the ingredient', 'maximum': 1000, 'minimum': 1, 'type': 'number'}, 'unit': {'description': 'The unit of the ingredient', 'enum': ['g', 'l', 'kg', 'n/a'], 'type': 'string'}}, 'required': ['name', 'quantity', 'unit'], 'type': 'object'}, 'minItems': 1, 'schema': 'http://json-schema.org/draft-07/schema#', 'type': 'array'}), recipes.validators.check_not_none_and_unique_ingredients]),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='title',
            field=models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(regex='^[a-zA-ZÀ-ú ]+$')]),
        ),
    ]
