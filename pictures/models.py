from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    profile_photo= models.ImageField(upload_to = 'images/', null=True)
    bio = models.CharField(max_length =30)
    name = models.CharField(max_length =30,null=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE ,related_name="profile",null=True)


    def __str__(self):
        return self.bio

    def save_profile(self):
        self.save()

    @classmethod
    def search_profile(cls, username):
        return cls.objects.filter(name__icontains=username)

    @classmethod
    def search_by_user(cls,search_term):
        profile = cls.objects.filter(title__icontains=search_term)
        return profile

    def save_profile(self):
        self.user
    def delete_profile(self):
        self.delete()

class Image(models.Model):
    image = models.ImageField(upload_to = 'images/',null=True )
    image_name = models.CharField(max_length =30)
    image_caption = models.CharField(max_length =30)
    user = models.ForeignKey(User,on_delete=models.CASCADE ,null=True )
    likes = models.IntegerField(default=0)
    
    

    def __str__(self):
        return self.image_name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_image(self):
        images = Image.objects.filter_by(id = 2).update(name = 'people')

    @classmethod
    def get_all_images(cls):
      images=cls.objects.all().prefetch_related('comment_set')
      return images

class Comments(models.Model):
    comment = models.CharField(max_length =30)
    user = models.ForeignKey(User,on_delete=models.CASCADE ,null=True )
    image = models.ForeignKey(Image,on_delete=models.CASCADE ) 
    

    def __str__(self):
        return self.comment