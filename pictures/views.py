from django.shortcuts import render
from .models import Image,Profile 
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/accounts/login/')
def image(request):
    images = Image.objects.all()
    print(images)
    return  render (request,'index.html',{"images":images})

def profile(request):
    return  render (request,'profile.html')

    
