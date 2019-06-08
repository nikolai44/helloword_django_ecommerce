from django.shortcuts import render
from products.models import *

# Create your views here.


def home(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True)
    products_images_iphones = products_images.filter(product__category__name="iPhone")
    products_images_macbooks = products_images.filter(product__category__name="MacBook")
    products_images_xiaomi = products_images.filter(product__category__name="Xiaomi")
    return render(request, 'landing/home.html', {'products_images_iphones': products_images_iphones,
                                                 'products_images_macbooks': products_images_macbooks,
                                                 'products_images_xiaomi': products_images_xiaomi
                                                 })
