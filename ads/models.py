from django.db import models


class Cat(models.Model):
    name = models.CharField(max_length=50)


class Ad(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    price = models.PositiveBigIntegerField()
    description = models.TextField(max_length=2000, null=True)
    address = models.CharField(max_length=300)
    is_published = models.BooleanField(default=False)
