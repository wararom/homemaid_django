from django.contrib import admin
from django.urls import path,include
from .views import ReserveMaid, homepage, CustomerRegis,SignUp,CustomerProfile,ListMaidView,viewmaidchoose,update_profile,slip,SlipView,getinfo
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('home/', homepage, name='home'),
    path('reserve/', ReserveMaid.as_view(), name='reserve'), 
    path('register/', CustomerRegis.as_view(), name='register'),
    path('viewpk/?P<pk>\+d/', ListMaidView.as_view(), name='viewpk'),
    path('viewmaid/', ListMaidView.as_view(), name='viewmaid'),
    path('viewprofile/', CustomerProfile.as_view(), name='viewprofile'),
    path('reserve_detail/', viewmaidchoose, name='viewmaidchoose'),
    path('update_profile', update_profile, name='update_profile' ),
    path('getinfo/', getinfo, name='getinfo'),
    path('slipform',SlipView.as_view(), name='slipform')
    # path('rent',rent,name='rent'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
