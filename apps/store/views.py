from django.shortcuts import render,get_object_or_404

from .models import Product, Category


def categoryDetail(request,slug):
    category = get_object_or_404(Category,slug=slug)
    products = category.products.all()

    context = {
        'category': category,
        'products': products
    }

    return render(request,'store/categories.html',context)


def productDetailView(request,category_slug,slug):

    product = get_object_or_404(Product,slug=slug)

    return render(request,'store/detail1.html',{'product':product})
