from django.db import models


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    def __str__(self):
        return self.username


class CartItem(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.CharField(max_length=1000)
    def __str__(self):
        return self.name


class Cart(models.Model):
    id = models.IntegerField(primary_key=True)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(CartItem)
    i = models.OneToOneField(CartItem, on_delete=models.CASCADE)

