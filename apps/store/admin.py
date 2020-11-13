from django.contrib import admin
from .models import Category, Product

admin.site.register(Category)



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title','price', 'category','tag') 
    list_filter = ('category',)