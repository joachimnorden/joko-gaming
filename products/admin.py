from django.contrib import admin
from .models import Product, Category

class ProductAdmin(admin.ModelAdmin):
    """ product model display """
    list_display = (
        'name',
        'category',
        'price',
        'review_count',
        'image'
    )

    search_fields = ('name', 'brand', 'price',)
    ordering = ('category',)


class CategoryAdmin(admin.ModelAdmin):
    """category model dissplay"""
    list_display = (
        'friendly_name',
        'name'
    )

    search_fields = ('friendly_name', 'name',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)

