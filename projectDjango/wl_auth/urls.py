from django.conf.urls import url
from . import views
from django.urls import path,include

urlpatterns = [
	path('signin/', views.signin, name='signin'),
	path('signout/', views.signout, name='signout'),
	path('change_password/', views.change_password, name='change_password'),
	
]