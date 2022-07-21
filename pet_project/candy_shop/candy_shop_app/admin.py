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


class PackageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_package')
    list_display_links = ('id', 'name_package')
    search_fields = ('name_package',)


class PriceAdmin(admin.ModelAdmin):
    list_display = ('id', 'prod', 'pack', 'price')
    list_display_links = ('id', 'prod')
    search_fields = ('prod',)
    list_filter = ('pack',)


class StorageAdmin(admin.ModelAdmin):
    list_display = ('id', 'prod', 'count_prod')
    list_display_links = ('id', 'prod')
    search_fields = ('prod',)


class FactoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'prod', 'pack', 'days')
    list_display_links = ('id', 'prod')
    search_fields = ('prod',)
    list_filter = ('pack', 'days')


class CitiesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_city', 'days')
    list_display_links = ('id', 'name_city')
    search_fields = ('name_city',)
    list_filter = ('days',)


admin.site.register(Production, ProductionAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Package, PackageAdmin)
admin.site.register(Price, PriceAdmin)
admin.site.register(Storage1, StorageAdmin)
admin.site.register(Storage2, StorageAdmin)
admin.site.register(Factory1, FactoryAdmin)
admin.site.register(Factory2, FactoryAdmin)
admin.site.register(Cities, CitiesAdmin)

admin.site.site_title = 'Админ-панель сайта кондитерских изделий'
admin.site.site_header = 'Админ-панель сайта кондитерских изделий'
