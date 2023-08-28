from django.urls import path
from .views import *


urlpatterns = [
    path('',service_page,name="service_page"),



    path('web_development',web_development,name="web_development"),
    path('web_development/Custom_Website_Development',Custom_Website_Development,name="Custom_Website_Development"),
    path('web_development/e_commerce_solutions',e_commerce_solutions,name="e_commerce_solutions"),
    path('web_development/responsive_design',responsive_design,name="responsive_design"),
    path('web_development/UI-UX_Excellence',uiux,name="uiux"),
    path('web_development/Web_Application_Innovation',web_app,name="web_app"),
    path('web_development/ongoing_optimization',ongoing_optimization,name="ongoing_optimization"),




    path('android_development',app_development,name="app_development"),
    path('android_development/Lifestyle_and_Convenience',Lifestyle_and_Convenience,name="Lifestyle_and_Convenience"),
    path('android_development/Learning_and_Information',learning,name="learning"),
    path('android_development/Productivity_and_Tools',productivity,name="productivity"),
    path('android_development/Entertainment_and_Media',entertainment,name="entertainment"),
    path('android_development/Practical_Solutions',pratical,name="pratical"),
    path('android_development/Enhanced_Experiences',ee,name="ee"),




    path('digital_marketing',marketing,name="marketing"),




] 