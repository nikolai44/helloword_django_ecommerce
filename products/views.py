from django.shortcuts import render
from products.models import *

# Create your views here.


def product(request, product_id):
    product = Product.objects.get_by_id(product_id)
    return render(request, "product/product_item.html")
