# Generated by Django 5.0.1 on 2024-01-30 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0002_remove_product_times_used_recipeproduct_times_cooked_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='recipeproduct',
            unique_together={('recipe', 'product')},
        ),
        migrations.AddField(
            model_name='product',
            name='times_used',
            field=models.IntegerField(default=0),
        ),
        migrations.RemoveField(
            model_name='recipeproduct',
            name='times_cooked',
        ),
    ]