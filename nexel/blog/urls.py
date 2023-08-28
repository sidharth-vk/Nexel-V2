from django.urls import path
from .views import *


urlpatterns = [
   path('',allblogs,name='allblogs'),
   path('<pk>',blogdetails,name='blogdetails')
] 