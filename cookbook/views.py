from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Recipe, Product, RecipeProduct

def add_product_to_recipe(request):
    if request.method == 'GET':
        recipe_id = request.GET.get('recipe_id')
        product_id = request.GET.get('product_id')
        weight = request.GET.get('weight')

        recipe = get_object_or_404(Recipe, pk=recipe_id)
        product = get_object_or_404(Product, pk=product_id)

        recipe_product, created = RecipeProduct.objects.get_or_create(recipe=recipe, product=product)
        recipe_product.weight = weight
        recipe_product.save()

        return HttpResponse(f"Product {product.name} added to recipe {recipe.name} with weight {weight}g.")

    return HttpResponse("Invalid request method.")

def cook_recipe(request):
    if request.method == 'GET':
        recipe_id = request.GET.get('recipe_id')

        recipe = get_object_or_404(Recipe, pk=recipe_id)

        # Увеличиваем количество приготовленных блюд для каждого продукта в рецепте на 1
        for product in recipe.products.all():
            product.dishes_count += 1
            product.save()

        return HttpResponse(f"Recipe {recipe.name} cooked successfully.")

    return HttpResponse("Invalid request method.")

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Recipe, Product, RecipeProduct

def show_recipes_without_product(request):
    if request.method == 'GET':
        product_id = request.GET.get('product_id')

        try:
            product = Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            return HttpResponse("Product not found.")

        # Находим рецепты, в которых продукт отсутствует или присутствует в количестве меньше 10 грамм
        recipes = Recipe.objects.exclude(recipeproduct__product=product).distinct()

        return render(request, 'cookbook/show_recipes_without_product.html', {'recipes': recipes, 'product': product})

    return HttpResponse("Invalid request method.")