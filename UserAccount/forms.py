from django import forms
from .models import *

class RegisterForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'phone', 'full_name', 'password']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'phone', 'full_name']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'date_of_birth', 'division', 'district', 'sub_district']
        

