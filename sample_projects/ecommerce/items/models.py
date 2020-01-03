from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    image = models.URLField(max_length=256, blank=True, null=True)
    price = models.FloatField()

    def __str__(self):
        return self.name
