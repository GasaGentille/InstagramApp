from django.test import TestCase
from .models import Image,Profile,Comments

# Create your tests here.

class ImageTestClass(TestCase):

    def setUp(self):
        # Creating a new image and saving it
        self.new_image= Image(image ='images/', image_name ='lady', image_caption = "so cute")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_image,Image))

    # Testing Save Method
    def test_save_image(self):
        self.new_image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0) 

    #test delete
    def test_delete_image(self):
        self.new_image.save_image()
        image = Image.objects.filter(image_name='lady').first()
        delete = Image.objects.filter(image_name = image.image_name).delete()
        images = Image.objects.all()
        self.assertFalse(len(images)==1)

    
    # Testing Update Method
    # def test_update_image(self):  
    #     self.new_image.save_image()
    #     image = Image.objects.filter(id = image.image_caption).update(image_caption = 'people').first()
    #     update = Image.objects.filter(image_caption=image.image_caption).update(image_caption='wonderfu')
    #     updated = Image.objects.filter(image_name='wonderful').first()
    #     self.assertNotEqual(image.image_caption, updated.image_caption) 

class ProfileTestCase(TestCase):
    # Set up method
    def setUp(self):
          self.new_profile=Profile(bio= "happiness in all")
        
        # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile,Profile))

    # Testing Save Method
    def test_save_profile(self):
        self.new_profile.save_profile()
        profile = Profile.objects.all()
        self.assertFalse(len(profile) > 0) 

    

    