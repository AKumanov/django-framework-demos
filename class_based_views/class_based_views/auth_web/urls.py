from django.urls import path
from . import views

urlpatterns = [
    path('', views.TodoIndexView.as_view(), name='index'),
    path('register/', views.UserRegisterView.as_view(), name='register'),
]