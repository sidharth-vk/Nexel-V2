from django.shortcuts import render,redirect
from django.http import HttpResponse
from blog.models import *
from .models import *

# Create your views here.


def homepage(request):
    blog = blogDetails.objects.order_by('?')[:3]
    ads_front = Front_page_ads.objects.order_by('?')[:1]
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
        'blog':blog,
        'ads_front':ads_front
    }
    return render(request,'index.html',context)





def team_page(request):
    teams = team.objects.all()
    context = {
        "teams":teams
    }
    return render(request,'team.html',context)


def contactuspage(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        interest = request.POST.get('interest')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        new_record = contactus.objects.create(name=name,email=email,phone=phone,service=interest,subject=subject,message=message)
        referer = request.META.get('HTTP_REFERER')
        return redirect(referer) if referer else redirect('contactus')
    return render(request,'contactus.html')



def aboutus(request):
    return render(request,'aboutus.html')

def privacypolicy(request):
    return render(request,'privacypolicy.html')



def why_choose_us(request):
    return render(request,'why_choose_us.html')