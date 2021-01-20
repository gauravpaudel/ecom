from django.db import models
from django.contrib.auth.models import User

from apps.store.models import Product


class Order(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    city = models.CharField(max_length = 100)
    address = models.CharField(max_length= 100)
    phone = models.CharField(max_length = 20)
    created_at = models.DateTimeField(auto_now_add= True)
    paid = models.BooleanField(default = False)
    cod = models.BooleanField(default = False)
    amount_to_be_paid = models.FloatField(blank = True, null = True)
    paid_amount = models.FloatField(blank = True, null=True)
    used_coupon = models.CharField(max_length = 50, blank = True, null = True)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)


class OrderItem(models.Model):
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE, blank=True, null=True)
    order = models.ForeignKey(Order, related_name='items', on_delete = models.CASCADE)
    product = models.ForeignKey(Product,related_name='items', on_delete=models.DO_NOTHING)
    price = models.FloatField()
    quantity = models.IntegerField(default = 1)
    
    statuss = [
        ('P','Placed'),
        ('S','Shipped'),
        ('D','Delivered')
    ]

    status = models.CharField(max_length =1, choices = statuss, default='P')


    def total_price(self):
        return self.price * self.quantity

    @property
    def date(self):
        return self.order.created_at

    def __str__(self):
        return '%s' % self.id
