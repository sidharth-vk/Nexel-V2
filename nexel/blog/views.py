from django.shortcuts import render
from .models import blogDetails
# Create your views here.
def blogdetails(request,pk):
    blog = blogDetails.objects.filter(slug=pk)
    context = {
        'blog':blog
    }
    return render(request,'blog/blogdetails.html',context)


def allblogs(request):
    blog = blogDetails.objects.all()
    context = {
        'blog':blog
    }
    return render(request,'blog/all_blogs.html',context)