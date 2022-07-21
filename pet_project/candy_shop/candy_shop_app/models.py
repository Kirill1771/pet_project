from django.db import models
from django.urls import reverse


class Production(models.Model):
    name_prod = models.CharField(max_length=50, verbose_name='Название')
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name='URL')
    compound = models.TextField(blank=True, verbose_name="Состав")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фотография")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Категория")

    def __str__(self):
        return self.name_prod

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = "Ассортимент"
        verbose_name_plural = "Ассортимент"
        ordering = ['name_prod']


class Category(models.Model):
    name = models.CharField(max_length=30, db_index=True, verbose_name="Категория")
    slug = models.SlugField(max_length=30, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['name']


class Package(models.Model):
    name_package = models.CharField(max_length=30, db_index=True, verbose_name="Вариант упаковки")

    def __str__(self):
        return self.name_package

    class Meta:
        verbose_name = "Упаковка"
        verbose_name_plural = "Упаковки"
        ordering = ['name_package']


class Price(models.Model):
    prod = models.ForeignKey('Production', on_delete=models.PROTECT, verbose_name="Продукция")
    pack = models.ForeignKey('Package', on_delete=models.PROTECT, verbose_name="Вариант упаковки")
    price = models.FloatField(max_length=20, verbose_name="Стоимость")

    def __str__(self):
        return self.price

    class Meta:
        verbose_name = "Стоимость"
        verbose_name_plural = "Стоимость"
        ordering = ['prod', 'pack', 'price']


class Storage1(models.Model):
    prod = models.ForeignKey('Production', on_delete=models.PROTECT, verbose_name="Продукция")
    pack = models.ForeignKey('Package', on_delete=models.PROTECT, verbose_name="Вариант упаковки")
    count_prod = models.IntegerField(verbose_name="Количество")

    class Meta:
        verbose_name = "Склад 1"
        verbose_name_plural = "Склад 1"
        ordering = ['prod']


class Storage2(models.Model):
    prod = models.ForeignKey('Production', on_delete=models.PROTECT, verbose_name="Продукция")
    count_prod = models.IntegerField(verbose_name="Количество")

    class Meta:
        verbose_name = "Склад 2"
        verbose_name_plural = "Склад 2"
        ordering = ['prod']


class Factory1(models.Model):
    prod = models.ForeignKey('Production', on_delete=models.PROTECT, verbose_name="Продукция")
    pack = models.ForeignKey('Package', on_delete=models.PROTECT, verbose_name="Вариант упаковки")
    days = models.FloatField(max_length=20, verbose_name="Количество дней")

    class Meta:
        verbose_name = "Фабрика 1"
        verbose_name_plural = "Фабрика 1"
        ordering = ['prod', 'days']


class Factory2(models.Model):
    prod = models.ForeignKey('Production', on_delete=models.PROTECT, verbose_name="Продукция")
    pack = models.ForeignKey('Package', on_delete=models.PROTECT, verbose_name="Вариант упаковки")
    days = models.FloatField(max_length=20, verbose_name="Количество дней")

    class Meta:
        verbose_name = "Фабрика 2"
        verbose_name_plural = "Фабрика 2"
        ordering = ['prod', 'days']


class Cities(models.Model):
    name_city = models.CharField(max_length=50, verbose_name='Название города')
    days = models.FloatField(max_length=20, verbose_name="Количество дней")

    def __str__(self):
        return self.name_city

    class Meta:
        verbose_name = "Название города"
        verbose_name_plural = "Название городов"
        ordering = ['name_city']

