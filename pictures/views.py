from django.shortcuts import render,redirect
from .models import Image,Profile 
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
from .forms import NewImageForm,ProfileForm


# Create your views here.

@login_required(login_url='/accounts/login/')
def image(request):
    images = Image.objects.all()
    print(images)
    return  render (request,'index.html',{"images":images})

@login_required(login_url='/accounts/login/')
def profile(request):
    profile = Profile.objects.all()
    return  render (request,'profile.html',{"profile":profile})

@login_required(login_url='/accounts/login/')
def new_image(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('/')

    else:
        form = NewImageForm()
    return render(request, 'new_image.html', {"form": form})

def add_profile(request):
    current_user = request.user
    title = 'Add profile'
    
    prof = Profile.objects.get(user_id =current_user.id)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        
        if form.is_valid():
            prof.profile_photo = form.cleaned_data['profile_photo']
            prof.username = form.cleaned_data['username']
            prof.save()
        return redirect('profile')

    else:
        form = ProfileForm()
    return render(request, 'profile.html', {"current_user":current_user,"title":title,"form": form})



# def sendEmail(request):
#     if request.method == 'POST':
#         form = NewsLetterForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['your_name']
#             email = form.cleaned_data['email']

#             recipient = NewsLetterRecipients(name = name,email =email)
#             recipient.save()
#             send_welcome_email(name,email)

#             HttpResponseRedirect('news_today')
#             #.................
#     return render(request, 'all-news/today-news.html', {"date": date,"news":news,"letterForm":form})
