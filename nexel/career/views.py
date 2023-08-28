from django.shortcuts import render,redirect
from .models import *
# Create your views here.


def career(request):
    data = career_form.objects.all()
    context = {
        'career':data
    }
    return render(request,'career/career.html',context)

def career_details(request,pk):
    data = career_form.objects.filter(slug=pk)
    context = {
        'career':data
    }
    return render(request,'career/careerdetails.html',context)



def allinternships(request):
    internship = internships.objects.all()
    youtubevideo = nexelyoutubelearn.objects.all()
    context={
        'internship':internship,
        "youtubevideo":youtubevideo
    }
    return render(request,'internships/all_internship.html',context)



def internships_details(request,pk):
    internship = internships.objects.filter(slug=pk)

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        linkedin = request.POST.get('linkedinurl')
        college = request.POST.get('College')
        haq = request.POST.get('haq')
        current_year = request.POST.get('current_year')
        internship_requested = pk
        cover_letter = request.POST.get('cover_letter')
        new_record = Internship_Registration.objects.create(name=name,email=email,phone=phone,linkedin=linkedin,college=college,haq=haq,current_year=current_year,internship=internship_requested,cover_letter=cover_letter)
        referer = request.META.get('HTTP_REFERER')
        return redirect(referer) if referer else redirect('contactus')





    context={
        'internship':internship
    }
    return render(request,'internships/internship_details.html',context)




def internship_upload(request):
    return render(request,'internships/internship_upload.html')