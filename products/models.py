from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255, null=True)
    category = models.ForeignKey('products.Category', on_delete=models.CASCADE)
    price = models.CharField(max_length=30, null=True)
    discount_price = models.CharField(max_length=30, null=True)
    description = models.TextField()
    color = models.CharField(max_length=15, null=True)
    size = models.CharField(max_length=5, null=True)
    count = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
