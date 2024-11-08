from django.db import models

# Create your models here.
class Student(models.Model):
    full_name = models.CharField(max_length=255)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=100)
    skills = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    password = models.CharField(max_length=128)  # Or use a hashed password

    def __str__(self):
        return self.full_name
    
class LoginRecord(models.Model):
    email = models.EmailField()  # Store the user's email
    password = models.CharField(max_length=128)  # This should ideally be hashed and not stored directly
    login_time = models.DateTimeField(auto_now_add=True)  # Automatically set the date/time when logging in

    def __str__(self):
        return f"{self.email} logged in at {self.login_time}"
    
from django.db import models


