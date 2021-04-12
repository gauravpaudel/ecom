from apps.cart.cart import Cart
from .models import Order, OrderItem


def checkout(request, first_name, last_name, email, city, address, phone):

    order = Order(
        first_name=first_name, last_name=last_name,
        email=email, city=city, address=address, phone=phone)
    order.save()

    cart = Cart(request)

    for item in cart:
        OrderItem.objects.create(
            order=order, product=item['product'], price=item['price'],
            quantity=item['quantity'], user=request.user)

    return order.id
