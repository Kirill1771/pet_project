from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class ProductionAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email',
                    'address', 'postal_code', 'city', 'paid',
                    'created', 'updated']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]


admin.site.register(Production, ProductionAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Order, OrderAdmin)

admin.site.site_title = 'Админ-панель сайта кондитерских изделий'
admin.site.site_header = 'Админ-панель сайта кондитерских изделий'
