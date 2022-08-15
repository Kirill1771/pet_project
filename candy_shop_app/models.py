from django.db import models
from django.urls import reverse


class Production(models.Model):
    name_prod = models.CharField(max_length=50, db_index=True, verbose_name='Название')
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name='URL')
    compound = models.TextField(blank=True, verbose_name="Состав")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True, verbose_name="Фотография")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Категория")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    stock = models.PositiveIntegerField(verbose_name="Остаток")
    available = models.BooleanField(default=True, verbose_name="Доступно")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Создано")
    updated = models.DateTimeField(auto_now=True, verbose_name="Обновлено")

    def __str__(self):
        return self.name_prod

    def get_absolute_url(self):
        return reverse('prod', kwargs={'prod_slug': self.slug})

    class Meta:
        verbose_name = "Ассортимент"
        verbose_name_plural = "Ассортимент"
        ordering = ['name_prod']
        index_together = (('id', 'slug'),)


class Category(models.Model):
    name = models.CharField(max_length=30, db_index=True, verbose_name="Категория")
    slug = models.SlugField(max_length=30, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('cat', kwargs={'prod_cat': self.slug})

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['name']
