from django.urls import path
from .views import *


urlpatterns = [
    path('',career,name="career"),
    path('jobopening/<pk>',career_details,name="careerdetails"),
    path('internships',allinternships,name="allinternships"),
    path('internships/upload',internship_upload,name="internship_upload"),
    path('internships/<pk>',internships_details,name="internships_details"),
] 