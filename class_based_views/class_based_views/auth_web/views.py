from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView, TemplateView

from class_based_views.auth_web.forms import CustomRegistrationForm

UserModel = get_user_model()


class TodoIndexView(TemplateView):
    template_name = 'auth/index.html'


class UserRegisterView(CreateView):
    template_name = 'auth/register.html'
    form_class = CustomRegistrationForm
