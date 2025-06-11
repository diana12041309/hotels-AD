from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.

class User(AbstractUser):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField(unique=True)
    phone = models.CharField(blank=True)
    password = models.CharField(max_length=128)
    date_joined = models.DateTimeField(default=timezone.now)
    date_of_birth = models.DateField(blank=True, null=True)
    gender_choices = [
        (1, 'Male'),
        (2, 'Female'),
        (3, 'Other')
    ]
    gender = models.IntegerField(choices=gender_choices, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f"{self.email}"
