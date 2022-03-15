from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import views as auth_views
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic as generic_views


class HomePageView(generic_views.TemplateView):
    template_name = 'index.html'


class UserRegisterView(generic_views.CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('index')


class UserLoginView(auth_views.LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('register')


class UserLogoutView(auth_views.LogoutView):
    template_name = 'logout.html'
