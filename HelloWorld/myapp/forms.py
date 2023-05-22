from django import forms
from django.contrib.auth.models import User
from .models import Car

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email']

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['year', 'model', 'type']
