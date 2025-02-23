from django.db import models


class Category(models.Model):
    cat_name = models.CharField(max_length=121)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.cat_name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=127)
    price = models.FloatField(default=0.0)
    stock = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to="products", blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.name
