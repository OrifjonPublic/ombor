from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    
    ROLE = (
        ("admin", "admin"),
        ("in", "in"),
        ("out", "out"),
        ("boss", "boss"),
    )

    role = models.CharField(max_length=20, choices=ROLE, default = 'user')

    def __str__(self):
        return self.role + ":  " + self.username
