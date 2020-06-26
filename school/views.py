from django.shortcuts import render
from .models import Photos, Notice


# Create your views here.

def photo(request):

    images = Photos.objects.all().order_by('-timeofspawn')
    return render(request,'photos.html',{'images':images})
 
def home(request):
    notice = Notice.objects.all()
    return render(request,'index.html',{'notice':notice})
