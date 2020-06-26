from django.shortcuts import render
from .models import Contact

def contact(request):

    name1 = Contact.objects.all()
    return render(request,'contact.html',{'name1':name1}) 
