from django.contrib import admin
from django.urls import path,include
from .views import MaidRegister,getinfomaid, SignUpMaid
from django.conf import settings
from django.conf.urls.static import static
from maid import views


urlpatterns = [    
    path('register/', MaidRegister.as_view(),name ='register'), 
    path('profilemaid/', views.getinfomaid,name ='profilemaid'), 
    path('signupmaid/', SignUpMaid.as_view() ,name ='signupmaid'),
    path('signin/', views.signin ,name='signin'),
    path('update_profile', views.update_profile, name='update_profile' ),
 
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
