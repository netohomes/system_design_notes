from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

