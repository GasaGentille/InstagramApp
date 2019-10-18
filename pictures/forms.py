from .models import Image
from django import forms

class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image_caption','image','user')