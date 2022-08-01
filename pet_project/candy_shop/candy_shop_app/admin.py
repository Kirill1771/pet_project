from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class ProductionAdmin(admin.ModelAdmin):
    list_display = ['name_prod', 'slug', 'price', 'stock', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name_prod',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Production, ProductionAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_title = 'Админ-панель сайта кондитерских изделий'
admin.site.site_header = 'Админ-панель сайта кондитерских изделий'
