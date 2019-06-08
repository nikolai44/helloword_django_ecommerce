from django.db import models
from django.contrib.auth.models import UserManager
from django.db.models import Sum, Count


class ProductImageManager(models.Manager):

    def get_by_product_id(self, product_id):
        return self.all().filter(product__id=product_id)

    def get_by_id(self, product_image_id):
        return self.all().filter(id=product_image_id)


class ProductManager(models.Manager):

    def get_by_id(self, product_id):
        return self.all().filter(product__id=product_id)


class ProductCategoryManager(models.Manager):

    def get_by_product_id(self, product_id):
        return self.all().filter(product__id=product_id)

    def get_by_id(self, product_category_id):
        return self.all().filter(id=product_category_id)
