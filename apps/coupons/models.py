from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Coupon(models.Model):

    code  = models.CharField(max_length=50)
    discount = models.IntegerField(validators = [MinValueValidator(0), MaxValueValidator(100)])
    active = models.BooleanField()
    num_available = models.IntegerField(default = 1)
    num_used = models.IntegerField(default=0)
    
    def __str__(self):
        return self.code
    
    def can_use(self):
        is_active = True

        if self.active == False:
            is_active = False
        
        if self.num_used >= self.num_available and self.num_available != 0:
            if_active = False
        
        return is_active
    
    def use(self):
        self.num_used += 1

        if self.num_used == self.num_available:
            self.active = False
        
        self.save()