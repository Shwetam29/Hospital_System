# from django.db import models
# from django.contrib.auth.models import AbstractUser



# class SIGNUP(models.Model):
#     firstname=models.CharField(max_length=50)
#     lastname=models.CharField(max_length=2)
#     # profile_picture =models.ImageField(required=False)
#     username=models.DateTimeField(auto_now_add=True)
#     email = models.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
#     password = models.CharField()
#     c_password = models.CharField()
#     address_line1 = models.CharField(max_length=255)
#     city = models.CharField(max_length=100)
#     state = models.CharField(max_length=100)
#     pincode = models.CharField(max_length=10)

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    user_type_choice=[
        ('D','DOCTOR'),
        ('P','PETIENT'),
    ]
    user_type=models.CharField(max_length=4,choices=user_type_choice,null="true")
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null="True")
    address_line1 = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    # Any additional fields specific to Patient can be added here

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)