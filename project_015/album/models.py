from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length = 256, unique=True)

    def __str__(self):
        return self.category_name

class Photo(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    name = models.CharField(max_length = 256, unique=True)
    url = models.URLField(max_length=200, unique=True)
    description = models.CharField(max_length = 2000, null = True)

    def __str__(self):
        return self.name;
