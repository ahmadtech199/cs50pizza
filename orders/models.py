from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User

# models.

class Product_catagory(models.Model):
    Catagory_name = models.CharField("Catagory Name",max_length=64)

    def __str__(self):
        return f"{self.Catagory_name}"

class Product(models.Model):
    catagory = models.ForeignKey(Product_catagory,on_delete=models.CASCADE,related_name="product_catagory")
    product_name = models.CharField(max_length=64)
    product_image = models.ImageField(verbose_name="Product Image",upload_to = "images/",default=None,blank=True)
    prize_small = models.DecimalField("Prize for Small",max_digits=5,decimal_places=2)
    prize_large = models.DecimalField("Prize for Large",max_digits=5,decimal_places=2)

    def __str__(self):
        return f"{self.product_name} -{self.catagory}"

class Topping(models.Model):
    topping_name = models.CharField("Topping",max_length=25)

    def __str__(self):
        return f"{self.topping_name}"

class Order(models.Model):
    STATUS = [
        ("P","Pending"),
        ("C","Complete"),
        ("D","Delivered")
    ]
    status = models.CharField(max_length=1,choices=STATUS,default="P")
    amount = models.IntegerField()
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_orders")

    def __str__(self):
        return f"{self.user} {self.status} {self.amount}"

class Order_detail(models.Model):
    order_detail = models.ForeignKey(Order,on_delete=models.CASCADE,related_name="order_details")
    product_detail = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="product_detail",default=0)
    quantity = models.IntegerField()
    rate = models.FloatField(default=0)
    topping = models.ManyToManyField(Topping,related_name="order_topping",blank=True)

    def __str__(self):
        return f"  {self.quantity} - {self.topping.in_bulk()}"


