from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    profile_photo= models.ImageField(upload_to = 'profile/', null=True)
    bio = models.CharField(max_length =30)

    def __str__(self):
        return self.location
        
    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    def update_location(self):
        location = Location.objects.filter_by(id = 2).update(location = 'kigali')


class Image(models.Model):
    image = models.ImageField(upload_to = 'images/',null=True )
    image_name = models.CharField(max_length =30)
    image_caption = models.CharField(max_length =30)
    user = models.ForeignKey(User,on_delete=models.CASCADE ,null=True )
    likes = models.IntegerField(default=0)
    comments = models.CharField(max_length =30)
    profile_photo =  models.ForeignKey(Profile, null=True)

    def __str__(self):
        return self.image_name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_image(self):
        images = Image.objects.filter_by(id = 2).update(name = 'people')



    

