from django.contrib import admin
from django.urls import path,include
from maid.views import *
from django.conf import settings
from django.conf.urls.static import static
from maid import views


urlpatterns = [    
    path('register/', MaidRegister.as_view(),name ='register'), 
    path('profilemaid/', views.getinfomaid,name ='profilemaid'), 
    path('signupmaid/', SignUpMaid.as_view() ,name ='signupmaid'),
    path('signinmaid/', signinmaid ,name='signinmaid'),
    path('signoutmaid/', signoutmaid ,name='signoutmaid'),
    path('update_maidprofile/', views.update_maidprofile, name='update_maidprofile' ),
    # path('retereview/' ,views.retereview, name='retereview'),
    path('retereview/', RateReviews.as_view(),name='ratereviews')
 
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
