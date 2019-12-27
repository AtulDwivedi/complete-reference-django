from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=256)
    image = models.URLField(max_length=256)

    def __str__(self):
        return self.name


class Item(models.Model):
    category = models.ForeignKey(
        Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    price = models.FloatField()
    image = models.URLField(max_length=256)

    def __str__(self):
        return self.name
