from .models import Image, Profile
from django import forms

class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image','image_caption','user')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_photo','bio')
        exclude=['user']
