from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import password_validation
UserModel = get_user_model()


class CustomRegistrationForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('username', 'password1', 'password2')
