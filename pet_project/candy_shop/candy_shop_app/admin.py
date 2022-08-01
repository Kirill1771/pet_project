from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class ProductionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_prod', 'slug', 'compound', 'get_html_photo', 'cat')
    list_display_links = ('id', 'name_prod')
    search_fields = ('name_prod',)
    list_filter = ('cat',)
    prepopulated_fields = {'slug': ('name_prod',)}

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")

    get_html_photo.short_description = 'Миниатюра'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
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
