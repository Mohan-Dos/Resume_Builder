from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('homepage/',homepage_fun,name='homepage'),
   
    path('getvalue/<int:id>',getvalue_fun,name='getvalue'),

    path('temp_1/',temp_1,name='temp_1'),
    path('temp_2/',temp_2,name='temp_2'),
    path('temp_3/',temp_3,name='temp_3'),
    path('temp_4/',temp_4,name='temp_4'),
    path('temp_5/',temp_5,name='temp_5'),
    
]

