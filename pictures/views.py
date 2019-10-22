from django.shortcuts import render,redirect
from .models import Image,Profile, Comments
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
def profile(request, username=None):
    current_user = request.user
    imgs = Image.objects.filter(user = current_user)
    print('aaaaaaaa')
    return  render (request,'profile.html',locals(),{"imgs":imgs})

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

@login_required(login_url='/accounts/login/')
def add_profile(request):
    current_user = request.user
    prof_update = Profile.objects.filter(user=current_user).first()
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
    
        if form.is_valid():
            image=form.save(commit=False)
            image.user=current_user
            image.save()
            
            return redirect('profile')
        
    else:
        print('gggggggg')

        form = ProfileForm()
    return render(request, 'add_profile.html', {"form": form})


@login_required(login_url='/accounts/login/')
def update_profile(request):
    current_user = request.user
    prof_update = Profile.objects.filter(user=current_user).first()
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
    
        if form.is_valid():
            profile=form.save(commit=False)
            Profile.objects.filter(id = prof_update.id).update(profile_photo =profile.profile_photo,bio=profile.bio)
            
            return redirect('profile')
        
    else:
        
        form = ProfileForm()
    return render(request, 'update.html', {"form": form})



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
