from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    
    REQUIRED_FIELDS = ['email', 'phone']
    USERNAME_FIELD = 'username'
    
    
    def __str__(self):
        return self.username