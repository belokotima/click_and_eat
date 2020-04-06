from django.db import models
from django.contrib.auth.models import User

# Create your models here.


def franchise_directory_path(instance, filename, subdir=None):
    """
    Метод, возвращающий путь, по которому будет сохранен файл
    :param instance: экземпляр Franchise
    :param filename: оригинальное название загруженного файла
    :param subdir: подпапка, в которой будет сохранен файл
    :return: путь, по которому будет сохранен файл
    """

    franchise_dir = 'franchise_{0}'.format(instance.id)

    if subdir is not None:
        return '{0}/{1}/{2}'.format(franchise_dir, subdir, filename)
    else:
        return '{0}/{1}'.format(franchise_dir, filename)


def franchise_data_directory_path(instance, filename):
    return franchise_directory_path(instance, filename, 'data')


def franchise_products_directory_path(instance, filename):
    return franchise_directory_path(instance, filename, 'products')


class Franchise(models.Model):
    title = models.CharField(max_length=32)
    logo = models.ImageField(upload_to=franchise_data_directory_path)
    preview_photo = models.ImageField(upload_to=franchise_data_directory_path)

    def get_restaurants(self):
        return Restaurant.objects.filter(franchise=self)


class ProductCategory(models.Model):
    title = models.CharField(max_length=32)


class ProductManager(models.Manager):
    def create_product(self, **kwargs):
        product = self.create(**kwargs)
        product.save()

        for restaurant in product.franchise:
            restaurant_product = RestaurantProduct.objects.create(restaurant=restaurant, product=product)
            restaurant_product.save()

        return product


class Product(models.Model):
    franchise = models.ForeignKey(Franchise, on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    photo = models.ImageField(upload_to=franchise_products_directory_path)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, null=True)
    weight = models.PositiveIntegerField()
    price = models.PositiveIntegerField()

    objects = ProductManager()


class Restaurant(models.Model):
    franchise = models.ForeignKey(Franchise, on_delete=models.CASCADE)
    address = models.CharField(max_length=128)
    manager_account = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    open_time = models.TimeField()
    close_time = models.TimeField()
    order_time = models.TimeField()


class RestaurantProduct(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    in_stock = models.BooleanField(default=True)
