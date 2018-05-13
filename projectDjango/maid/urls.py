from django.contrib import admin
from django.urls import path,include
from .views import MaidRegister,getAllinfo
from django.conf import settings
from django.conf.urls.static import static
from maid import views


urlpatterns = [    
    path('register/', MaidRegister.as_view(),name ='register'), 
    path('profilemaid/', views.getAllinfo,name ='profilemaid'), 
 
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
