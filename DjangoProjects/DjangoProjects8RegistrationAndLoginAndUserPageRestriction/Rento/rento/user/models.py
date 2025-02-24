from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    
    GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
    ]
    status = [
    ('blocked', 'Blocked'),
    ('clear', 'Clear'),
    ]

    location = models.CharField(max_length=120)
    gender = models.CharField(
        choices=GENDER_CHOICES, 
        max_length= 120, 
        null= True
    )
    phone_number = models.CharField(max_length=120)
    user_status = models.CharField(
        max_length=20, choices=status, default='clear')