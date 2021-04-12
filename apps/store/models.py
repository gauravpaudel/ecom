from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    ordering = models.IntegerField(default=0)
    image = models.ImageField(upload_to='uploads/category', null=True, blank=True)
    is_featured = models.BooleanField(default=False)
    description = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ('ordering',)
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('categories_detail',args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        return super().save(*args, **kwargs)


class Product(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='products')
    parent = models.ForeignKey(
        'self', 
        related_name='variants',
        on_delete=models.CASCADE,
        null=True, blank=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    old_price = models.FloatField()
    price = models.FloatField()
    num_available = models.IntegerField(default=1)
    tags = [
        ('new', 'new'),
        ('best_seller', 'best seller'),
        ('out_of_stock', 'out of stock'),
        ('available', 'available')
    ]

    tag = models.CharField(max_length=20, choices=tags, default='available')
    is_featured = models.BooleanField(default=True)
    date_added = models.DateTimeField(auto_now_add=True)
    description = models.TextField(default='')
    image = models.ImageField(upload_to='uploads', blank=True, null=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads', blank=True, null=True)

    def __str__(self):
        return self.product.title
