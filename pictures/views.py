from django.shortcuts import render
from .models import Image,Profile 


# Create your views here.

def image(request):
    images = Image.objects.all()
    print(images)
    return  render (request,'index.html',{"images":images})

def profile(request):
    return  render (request,'profile.html')

    
