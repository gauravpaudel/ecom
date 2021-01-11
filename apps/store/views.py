from django.shortcuts import render,get_object_or_404,redirect

from .models import Product, Category


def categoryDetail(request,slug):
    category = get_object_or_404(Category,slug=slug)
    products = category.products.all()



    context = {
        'category': category,
        'products': products
    }

    return render(request,'store/cat.html',context)


def productDetailView(request,category_slug,slug):

    product = get_object_or_404(Product,slug=slug)

    if product.parent:
        return redirect('product_detail', category_slug=category_slug,slug=product.parent.slug)


    imagesstring = "{'image': '%s'}," % (product.image.url)

    for image in product.images.all():
        imagesstring += "{'image': '%s'}," % (image.image.url)



    context = {
        'product': product,
        'istring': imagesstring
    }


    return render(request,'store/detail1.html',context)
