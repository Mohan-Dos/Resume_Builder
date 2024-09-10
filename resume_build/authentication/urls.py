from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
   
    path('',landign_page_fun,name='landing_page'),
    path('login/',login_fun,name='loginpage'),
    path('register/',register_fun,name='registerpage'),
    
    path('logoutpage/',logout_fun,name='logout_page')
    
]