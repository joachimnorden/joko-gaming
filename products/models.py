from django.db import models
from django.contrib.auth.models import User
from profiles.models import UserProfile


class Category(models.Model):
    """ category models """
    class Meta:
        """ add correct plural name"""
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """ products model """
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    brand = models.CharField(max_length=254)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    sale_price = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True
        )
    discount = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True
        )
    is_new = models.BooleanField(default=True)
    has_colors = models.BooleanField(default=False, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True
        )
    review_count = models.DecimalField(
        max_digits=6, decimal_places=0, null=True, blank=True, default=0
        )
    sort_price = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True
        )
    add_to_whishlist = models.ManyToManyField(
        User, related_name='whishlist_add', blank=True
        )

    def __str__(self):
        return self.name


class Review(models.Model):
    """ A review model for users to review products """

    RATING = [
        (5, '5'),
        (4, '4'),
        (3, '3'),
        (2, '2'),
        (1, '1'),
    ]

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING, default=3)
    body = models.TextField(max_length=1024)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'User: {self.user} rated {self.product}, {self.product} stars.'
