from django.shortcuts import render
from apps.cart.cart import Cart

def cart_detail(request):
    cart  = Cart(request)

    productsstring = ''

    for item in cart:
        product = item['product']
        b = "{'id': '%s', 'title': '%s', 'price': '%s', 'quantity': '%s','total_price':'%s','image':'%s'}," % (product.id,product.title,product.price,item['quantity'],item['total_price'],product.image.url)
        
        productsstring += b
    
    context = {
        'cart': cart,
        'productsstring': productsstring
    }

    return render(request,'cart/cart1.html',context)


def tests(request):
    return render(request,'cart/cart1.html')