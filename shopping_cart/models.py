from django.contrib.auth.models import User
# from django.db import models

# from shop.models import Product

# Create your models here.

# class Cart(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return f'Cart {self.id} for {self.user.username if self.user else 'Anonymous'}'
#
# class CartItem(models.Model):
#     cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)
#
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     def total_amount(self):
#         if self.product.discounted_price:
#             return self.quantity * self.product.discounted_price
#         return self.quantity * self.product.price
#
#     def __str__(self):
#         return f'{self.quantity} x {self.product.name} in Cart {self.cart.id}'
#
# class Order(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
#     ordered_at = models.DateTimeField(auto_now_add=True)
#     total_amount = models.PositiveIntegerField(default=0)
