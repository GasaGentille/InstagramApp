from django.shortcuts import render
from .models import Image,Profile 
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
from .forms import NewImageForm

# Create your views here.

@login_required(login_url='/accounts/login/')
def image(request):
    images = Image.objects.all()
    print(images)
    return  render (request,'index.html',{"images":images})

@login_required(login_url='/accounts/login/')
def profile(request):
    return  render (request,'profile.html')

@login_required(login_url='/accounts/login/')
def new_image(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('NewImage')

    else:
        form = NewImageForm()
    return render(request, 'new_image.html', {"form": form})
