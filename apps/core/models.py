from django.db import models

# Create your models here.

class Cams(models.Model):
    name = models.CharField(max_length=25)
    place = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name + "  ( " + self.place + " ) "  



class IceCream(models.Model):
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100, unique=True)
    quantity = models.PositiveIntegerField(default=0)
    camera = models.ForeignKey(Cams, null=True, blank=True, on_delete=models.CASCADE)
    size_per_box = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity} ta {self.name}"

