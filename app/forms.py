# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.forms import ModelForm
# from app.models import SIGNUP

# class SIGNUPForm(ModelForm):
#     class Meta:
#         model=SIGNUP
#         fields=['firstname','lastname','email','password ','c_password ',' address_line1 ','city ','state ','pincode ']

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserSignUpForm(UserCreationForm):
    # user_type=forms.CharField(max_length=2,choices=user_type_choice)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    profile_picture = forms.ImageField(required=False)
    address_line1 = forms.CharField(max_length=255)
    city = forms.CharField(max_length=100)
    state = forms.CharField(max_length=100)
    pincode = forms.CharField(max_length=10)

    class Meta:
        model = User
        fields = ('user_type','first_name', 'last_name', 'username', 'email', 'password1', 'password2',
                  'profile_picture', 'address_line1', 'city', 'state', 'pincode')