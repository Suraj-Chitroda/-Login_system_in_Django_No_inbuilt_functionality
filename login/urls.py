from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.loginme, name='login'),
    path('register', views.register, name='register'),
    path('home', views.home, name='home'),
    path('logout', views.logout, name='logout')
]
