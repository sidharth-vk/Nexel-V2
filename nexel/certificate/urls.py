from django.urls import path
from .views import *


urlpatterns = [
   path('verify/nexel_certificateid=<pk>',verify,name="verify"),
   path('verify/nexel_offerletterid=<pk>',verify_offerletter,name="verify_offerletter")
] 