from django.contrib import admin
from django.urls import path,include
from .views import ReserveMaid, homepage

urlpatterns = [

    path('home/', homepage, name='home'),
    path('reserve/', ReserveMaid, name='reserve-maid'), 
]
