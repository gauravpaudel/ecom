from django.contrib import admin
from .models import Category, Product, ProductImage


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['title']
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'category', 'tag')
    list_filter = ('category',)
    search_fields = ['title']
    list_editable = ['price', 'tag']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(ProductImage)
