from django.urls import path
from .views import *


urlpatterns = [
   path('',homepage,name="home"),
   path('why_choose_us',why_choose_us,name="why_choose_us"),
   path('our_team',team_page,name="team"),
   path('Contact_us',contactuspage,name="contactus"),
   path('about_nexel',aboutus,name="aboutus"),
   path('nexel-privacy-policy',privacypolicy,name="privacypolicy"),
] 