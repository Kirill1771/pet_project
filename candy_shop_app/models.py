from django.urls import reverse
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    _metadata = {
        'description': 'description',
    }

    class Meta:
        verbose_name_plural = 'Categories'

    def get_absolute_url(self):
        return reverse('products:index', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name


class ProductionQuerySet(models.QuerySet):
    def active(self):
        return self.filter(is_active=True)


class ProductionManager(models.Manager):
    def get_queryset(self):
        return ProductionQuerySet(self.model, using=self.db)

    def all(self):
        return self.get_queryset().active()


class Production(models.Model):
    name_prod = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now=True, db_index=True)
    updated_at = models.DateTimeField(auto_now_add=True, db_index=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    content = models.TextField(verbose_name='Content Description')
    category = models.ManyToManyField(Category, blank=True)
    is_active = models.BooleanField(default=True, verbose_name='Active')
    is_featured = models.BooleanField(default=False, verbose_name='Featured')

    objects = ProductionManager()

    _metadata = {
        'description': 'content',
    }

    class Meta:
        ordering = ['-created_at']

    @property
    def get_image_url(self):
        return self.image.url

    def get_absolute_url(self):
        return reverse('products:detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name