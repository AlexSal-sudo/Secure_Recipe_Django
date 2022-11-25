# Generated by Django 4.1.3 on 2022-11-25 17:20

from django.db import migrations
import jsonfield.fields
import recipes.validators


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_alter_recipe_ingredients'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=jsonfield.fields.JSONField(default={}, validators=[recipes.validators.validate_ingredient]),
        ),
    ]
