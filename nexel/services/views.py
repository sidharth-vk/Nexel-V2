from django.shortcuts import render,redirect
from django.http import HttpResponse
from blog.models import blogDetails
from homepages.models import * 
# Create your views here.

# web development
def web_development(request):
    blog = blogDetails.objects.order_by('?')[:3]
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        interest = request.POST.get('interest')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        new_record = contactus.objects.create(name=name,email=email,phone=phone,service=interest,subject=subject,message=message)
        referer = request.META.get('HTTP_REFERER')
        return redirect(referer) if referer else redirect('home')
    context = {
       "blog":blog 
    }
    return render(request,'services/web.html',context)


# web detail
def Custom_Website_Development(request):
    return render(request,'services/web/cwd.html')

def e_commerce_solutions(request):
    return render(request,'services/web/e_commerce.html')

def responsive_design(request):
    return render(request,'services/web/responsive_design.html')

def uiux(request):
    return render(request,'services/web/uiux.html')

def web_app(request):
    return render(request,'services/web/web_app.html')

def ongoing_optimization(request):
    return render(request,'services/web/ongoing_optimization.html')





# app development
def app_development(request):
    blog = blogDetails.objects.order_by('?')[:3]
    context = {
       "blog":blog 
    }
    return render(request,'services/android.html',context)

def Lifestyle_and_Convenience(request):
    return render(request,'services/android/lifestyle_and_Convenience.html')

def learning(request):
    return render(request,'services/android/learning.html')

def productivity(request):
    return render(request,'services/android/productivity.html')

def entertainment(request):
    return render(request,'services/android/entertainment.html')

def pratical(request):
    return render(request,'services/android/pratical.html')

def ee(request):
    return render(request,'services/android/ee.html')





# marketing
def marketing(request):
    blog = blogDetails.objects.order_by('?')[:3]
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        interest = request.POST.get('interest')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        new_record = contactus.objects.create(name=name,email=email,phone=phone,service=interest,subject=subject,message=message)
        referer = request.META.get('HTTP_REFERER')
        return redirect(referer) if referer else redirect('home')
    context = {
       "blog":blog 
    }
    return render(request,'services/marketing.html',context)













def service_page(request):
    return render(request,'services/service_page.html')