from django.shortcuts import render, get_object_or_404
from .models import Product

def all_products(request):
    """ A view to show all products, including sorting and searching queries"""

    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'products.html', context)


def product_details(request, product_id):
    """ A view to show product details"""

    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product,
    }
    return render(request, 'product_details.html', context)
