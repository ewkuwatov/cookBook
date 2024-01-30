# Generated by Django 5.0.1 on 2024-01-30 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0004_alter_recipeproduct_unique_together_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='products',
            field=models.ManyToManyField(through='cookbook.RecipeProduct', to='cookbook.product'),
        ),
    ]
