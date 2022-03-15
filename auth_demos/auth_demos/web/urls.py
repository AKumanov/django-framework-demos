from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='index'),
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
]
