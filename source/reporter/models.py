from django.contrib.auth.models import User
from django.db import models


CATEGORY_CHOICES = (
    ('other', 'Other'),
    ('food', 'Food'),
    ('clothes', 'Clothes'),
    ('household', 'Home items'),
)


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Product')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default=CATEGORY_CHOICES[0][0],
                                verbose_name='Category')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Description')
    photo = models.ImageField(upload_to='uploads', null=True, blank=True, verbose_name='Photo')

    def __str__(self):
        return self.name


class Review(models.Model):
    author = models.ForeignKey(User, related_name='reporter', on_delete=models.CASCADE, verbose_name='Author')
    product = models.ForeignKey(Product, related_name='product', on_delete=models.CASCADE, verbose_name='Product')
    feedback = models.TextField(max_length=2000, verbose_name='Feedback')
    point = models.IntegerField(null=False, blank=False, verbose_name='Point')

    def __str__(self):
        return str(self.author)