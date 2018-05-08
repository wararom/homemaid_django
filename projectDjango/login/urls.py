from django.contrib import admin
from django.urls import path,include
from .views import login, auth_view, logout, loggedin, invalid_login, register_user, register_success
urlpatterns = [
    
    # auth
    path('login/',  login, name='login'),
    path('auth/',  auth_view,name='auth'),    
    path('logout/', logout,name='logout'),
    path('loggedin/', loggedin,name='logged'),
    path('invalid/', invalid_login,name='inlalid'),    
    path('register/', register_user,name='regis'),
    path('register_success/', register_success,name='regissuccess'),
]