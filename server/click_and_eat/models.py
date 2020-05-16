from django.db import models
from django.contrib.auth.models import User


# Create your models here.


def restaurant_directory_path(instance, filename, subdir=None):
    """
    Метод, возвращающий путь, по которому будет сохранен файл
    :param instance: экземпляр Franchise
    :param filename: оригинальное название загруженного файла
    :param subdir: подпапка, в которой будет сохранен файл
    :return: путь, по которому будет сохранен файл
    """

    franchise_dir = 'restaurant_{0}'.format(instance.id)

    if subdir is not None:
        return '{0}/{1}/{2}'.format(franchise_dir, subdir, filename)
    else:
        return '{0}/{1}'.format(franchise_dir, filename)


def restaurant_data_directory_path(instance, filename):
    return restaurant_directory_path(instance, filename, 'data')


def restaurant_products_directory_path(instance, filename):
    return restaurant_directory_path(instance, filename, 'products')


def product_directory_path(instance, filename):
    return restaurant_products_directory_path(instance.restaurant, 'product{}_{}'.format(instance.id, filename))


class Restaurant(models.Model):
    """
    Модель ресторана. Рассматриваем ее как главную модель в бд

    title, description, logo, open/close time - понятно
    owner - вы делаете, чтобы у каждого был владелец. Это вроде ок, но кто владелец условно у макдональса?
            Они будут зареганы как отдельная организация. Однако это детали, на первое время - норм
    address - его здесь нет и не будет. Для этого будет следующая таблица. Так мы легко сможем решить вопрос с сетями
    """
    title = models.CharField(max_length=256)
    description = models.CharField(max_length=1024)
    logo = models.ImageField(upload_to=restaurant_data_directory_path)
    preview_image = models.ImageField(upload_to=restaurant_data_directory_path)
    open_time = models.TimeField()
    close_time = models.TimeField()

    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.pk is None:
            saved_logo = self.logo
            saved_preview = self.preview_image
            self.logo = None
            self.preview_image = None
            super(Restaurant, self).save(*args, **kwargs)
            self.logo = saved_logo
            self.preview_image = saved_preview

        super(Restaurant, self).save(*args, **kwargs)

    def get_products(self):
        return Product.objects.filter(restaurant=self)

    def get_no_category_products(self):
        return Product.objects.filter(restaurant=self, category=None)

    def has_no_category_products(self):
        return len(self.get_no_category_products()) > 0

    def get_categories(self):
        return Category.objects.filter(restaurant=self)

    def get_addresses(self):
        return AddressOfRestaurant.objects.filter(restaurant=self)


class AddressOfRestaurant(models.Model):
    """
    Модель, которая решит проблемы сетевых ресторанов. Если ресторан один, то будет просто один адрес и все.
    Если много, то будете предлагать пользователю выбирать/ближайший к его геолокации
    """
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    address = models.CharField(max_length=256)
    longitude = models.FloatField(default='1')
    latitude = models.FloatField(default='1')


class Category(models.Model):
    """
    Подгялдел у вас. Разделить блюда на закуски/горячие/напитки - хорошая идея
    """
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)

    def get_products(self):
        return self.restaurant.get_products().filter(category=self)


class Product(models.Model):
    """
    Ресторан будет добавлять блюда сколько хотят. Мы просто будем выводить их все пользователю

    name, photo, price - тоже ясно
    value - у тебя был weight, все-таки надо писать общую модель. У напитка, например, не вес, а объем
    """
    name = models.CharField(max_length=32)
    photo = models.ImageField(upload_to=product_directory_path, null=True)
    description = models.CharField(max_length=1024, default='')
    price = models.PositiveIntegerField()
    value = models.CharField(max_length=16)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.pk is None:
            saved_photo = self.photo
            self.photo = None
            super(Product, self).save(*args, **kwargs)
            self.photo = saved_photo

        super(Product, self).save(*args, **kwargs)


class Profile:
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(AddressOfRestaurant, on_delete=models.CASCADE)
    secret_code = models.CharField(max_length=8)
    order_time = models.DateTimeField(auto_now_add=True)
    pickup_time = models.DateTimeField()
    order_close_time = models.DateTimeField()

    def get_products(self):
        return OrderProduct.objects.filter(order=self)


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
