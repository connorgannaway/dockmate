from os import name
from django.db import models
from django.contrib.auth.models import User
from PIL import Image

#Model classes are tables objects in a database.
#each variable is a column and its datatype.
#__str__ method defines the name of a object (row) in a database table

#profile model is meant to be used as an extension to the User model
#this is so users can have a profile picture and be connected to a company

class Company(models.Model):
    name = models.CharField(max_length=50, unique=True)
    key = models.CharField(max_length=12, unique=True)

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(default='default.jpg', upload_to='profile_pics')
    company = models.OneToOneField(Company, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

    #overriding save method to resize image before saving.
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        image = Image.open(self.picture.path)
        if image.width > 300 or image.height > 300:
            image.thumbnail((300, 300))
            image.save(self.picture.path)
