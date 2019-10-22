from .models import Image, Profile,Comments
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

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_photo','bio')
        exclude=['user']

class CommentForm(forms.ModelForm):
  class Meta:
      model=Comments
      exclude=['image','user']