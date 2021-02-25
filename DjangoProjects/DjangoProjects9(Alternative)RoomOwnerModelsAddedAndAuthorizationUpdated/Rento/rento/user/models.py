from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.


class RoomOwner(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    # group = models.ForeignKey(Group, on_delete=models.CASCADE, default=1)
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
        null= True,
        blank= True
    )
    phone_number = models.CharField(max_length=120)
    user_status = models.CharField(
        max_length=20, choices=status, default='clear')
    
    def __str__(self):
        return self.user.username
    