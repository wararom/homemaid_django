from django.contrib import admin
from django.urls import path,include
from customer.views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('success/', success, name='success'),
    path('reserve/', ReserveMaid.as_view(), name='reserve'), 
    path('reservemaid/<int:pkmaid>', update_reserve, name='reserve'), 
    path('viewmaid/', ListMaidView.as_view(), name='viewmaid'),
    path('viewprofile/', CustomerProfile.as_view(), name='viewprofile'),
    path('update_profile/', update_profile, name='update_profile' ),
    path('detail_reserve/', getinfo, name='detail_reserve'),
    path('slipform',SlipView.as_view(), name='slipform'),
    path('signin/', signin, name='signin'),
	path('signout/', signout, name='signout'),

    # path('rent',rent,name='rent'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
