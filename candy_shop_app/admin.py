from django.contrib import admin

from .models import Category, Production


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}


class ProductionAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name_prod',)}
    list_display = ('name_prod', 'sku', 'price', 'slug', 'is_active',)
    ordering = ['-is_active', 'name_prod']
    list_filter = ('is_active',)


admin.site.register(Production, ProductionAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_title = 'Админ-панель сайта кондитерских изделий'
admin.site.site_header = 'Админ-панель сайта кондитерских изделий'
