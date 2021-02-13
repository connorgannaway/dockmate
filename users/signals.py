from django.db.models.signals import post_save, pre_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile
import os
from dockmate.settings import BASE_DIR

#signals watch for events anywhere in the app, and then act on them
#event is defined in 1st var of @reciever

#when user registers, entry to User model is created, but not Profile model.
@receiver(post_save, sender=User)
def createProfileFromUser(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

#save the created profile from above
@receiver(post_save, sender=User)
def saveProfile(sender, instance, **kwargs):
    instance.profile.save()
