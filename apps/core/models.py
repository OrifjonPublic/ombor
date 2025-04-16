from django.db import models

# Create your models here.

class Cams(models.Model):
    name = models.CharField(max_length=25)
    place = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name + "  ( " + self.place + " ) "  



class IceCream(models.Model):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)
    camera = models.ForeignKey(Cams, null=True, blank=True, on_delete=models.CASCADE)
    size_per_box = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity} ta {self.name}"

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['code', 'name', 'camera'], name='unique_ice_combination')
        ]

from django.contrib.auth import get_user_model

User = get_user_model()

class ActionLog(models.Model):
    ACTION_TYPES = (
        ('create', 'Create'),
        ('update', 'Tahrirlandi'),
        ('delete', "O'chirildi"),
        ('in', 'Kirim'),
        ('out', 'Chiqim'),
    )

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    action = models.CharField(max_length=10, choices=ACTION_TYPES)
    object_name = models.CharField(max_length=100)  # 👉 mahsulot nomi (IceCream.name)
    object_id = models.CharField(max_length=50)     # code
    object_repr = models.TextField()                # tavsif
    quantity = models.PositiveIntegerField(default=0)  # qancha o‘zgarish bo‘lgan
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.action} - {self.object_name} - {self.quantity} - {self.timestamp}"
