import json

from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string 

from apps.cart.cart import Cart
from .models import Product
from apps.order.models import Order, OrderItem

from apps.order.utils import checkout

def api_add_to_cart(request):
    data = json.loads(request.body)
    jsonresponse = {'success':True}
    product_id = data['product_id']
    quantity = data['quantity']
    update = data['update']

    cart = Cart(request)

    product = get_object_or_404(Product, pk=product_id)

    if not update:
        cart.add(product=product,quantity=1, update_quantity = False )

    else:
        cart.add(product = product, quantity = quantity, update_quantity = True )
    
    return JsonResponse(jsonresponse)


def api_checkout(request):

    cart = Cart(request)

    data = json.loads(request.body)
    jsonresponse = {'success':True}
    first_name = data['first_name']
    last_name = data['last_name']
    email = data['email']
    city = data['city']
    address = data['address']   
    phone = data['phone']
    orderid = checkout(request, first_name, last_name, email, city, address, phone)

    paid = True

    if paid:
        order = Order.objects.get(pk = orderid)
        order.paid = True
        order.paid_amount = cart.get_total_cost()
        order.save()
        html = render_to_string('core/email_confirmation.html')
        send_mail('Order Confirmation','Your order has been sent','noreply@mpasal.com',['mail@mpasal.com',order.email],fail_silently=True,html_message=html)
        cart.clear()
    
    return JsonResponse(jsonresponse)


def api_remove_from_cart(request):

    cart = Cart(request)
    
    data = json.loads(request.body)
    jsonresponse = {'success':True}
    product_id  = str(data['product_id'])

    cart = Cart(request)
    cart.remove(product_id)
   
    return JsonResponse(jsonresponse)
