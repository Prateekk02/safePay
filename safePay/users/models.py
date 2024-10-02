from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager

class CustomUser(AbstractUser):
    
    username = None
    
    # Custom Field
    email = models.EmailField()
    phone_no = models.CharField(max_length=10, unique=True)
    phone_verified = models.BooleanField(default=False)    
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    address_line_1 = models.CharField(max_length=100)
    address_line_2 = models.CharField(max_length=100)
    dob = models.DateField()
    
    USERNAME_FIELD = 'phone_no' 
    REQUIRED_FIELDS = []
    
    # Using Custom Manager 
    objects = UserManager()
    
    def __str__(self):
        return self.phone_no
    