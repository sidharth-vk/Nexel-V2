from career.models import internships
from services.models import serviceAds

from django.shortcuts import render,redirect

from homepages.models import *

def navbar_data(request):
    internship =internships.objects.all()[:5]
    return {
        'internship':internship
    }


def serviceads(request):
    ads = serviceAds.objects.order_by('?').first()

    return {
        "ads":ads
    }


