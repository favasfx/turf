from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('test', views.user,name= 'user'),

    path('', views.index,name= 'index'),

    path('booking', views.booking,name='booking'),

    path('login', views.login,name='login'),

    path('home', views.home,name='home'),

    path('signin', views.signin,name='signin'),


]