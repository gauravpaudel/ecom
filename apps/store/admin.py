from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['title']
    search_fields = ['title']



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title','price', 'category','tag') 
    list_filter = ('category',)
    search_fields = ['title']
    list_editable = ['price','tag']