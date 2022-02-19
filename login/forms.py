# Taken from tutorial 
# see: https://www.techwithtim.net/tutorials/django/user-registration/
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]