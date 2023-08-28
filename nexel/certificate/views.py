from django.shortcuts import render
from .models import *
# Create your views here.
def verify(request,pk):
    certificates = certificate.objects.filter(slug=pk)
    context = {
        'certificates':certificates
    }
    return render(request,'certificate/verify.html',context)

def verify_offerletter(request,pk):
    offerletters = offerletter.objects.filter(slug=pk)
    context = {
        'offerletters':offerletters
    }
    return render(request,'certificate/offerletter.html',context)