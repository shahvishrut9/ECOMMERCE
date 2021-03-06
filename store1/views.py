from category.models import Category
from django.shortcuts import get_list_or_404, render
from .models import Product

# Create your views here.


def store1(request, category_slug=None):
    categories = None
    products = None

    if category_slug != None:
        categories = get_list_or_404(Category, slug=category_slug)
        products = Product.objects.filter(
            category=categories, is_available=True)
        product_count = products.count()

    else:
        products = Product.objects.all().filter(is_available=True)
        product_count = products.count()

    context = {
        'products': products,
        'product_count': product_count,
    }
    return render(request, 'store1/store1.html', context)
