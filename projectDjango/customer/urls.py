from django.contrib import admin
from django.urls import path,include
from .views import ReserveMaid, homepage, CustomerRegis,SignUp,CustomerProfile,ListMaidView

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('home/', homepage, name='home'),
    path('reserve/', ReserveMaid.as_view(), name='reserve'), 
    path('register/', CustomerRegis.as_view(), name='register'),
    path('viewpro/', ListMaidView.as_view(), name='viewpro'),
]
