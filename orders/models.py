from django.db import models
from account.models import CustomUser
from products.models import Product


class Order(models.Model):
    STATUES = [

        ('PENDING', 'pending'),
        ('INPROGRESS', 'inprogress'),
        ('COMPLATED', 'complated'),
        ('CANCELED', 'canceled')
    ]

    customor = models.ForeignKey('account.CustomUser', on_delete=models.SET_NULL, null=True, related_name='orders')
    order_date = models.DateTimeField(auto_now_add=True)
    required_date = models.DateTimeField(null=True)
    shipped_date = models.DateTimeField(null=True)
    canceled_data = models.DateTimeField(null=True)
    status = models.CharField(max_length=10, choices=STATUES)

    def __str__(self):
        return f'{self.customor.__str__()} --order_id :{self.id}'

    def item_count(self):
        return self.details.count()

    def total_price(self):
        return sum([i.total_price() for i in self.details.all()])


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='details')
    product = models.ForeignKey('products.Product', on_delete=models.SET_NULL,null=True, related_name='orders')
    quantity = models.IntegerField(default=1)

    def total_price(self):
        return self.product.price*self.quantity

    def __str__(self):

        return f'order:{self.order} -- {self.product} --quantity : {self.quantity}'