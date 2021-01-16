from django.db.models.signals import post_save, pre_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile
import os
from dockmate.settings import BASE_DIR

@receiver(post_save, sender=User)
def createProfileFromUser(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def saveProfile(sender, instance, **kwargs):
    instance.profile.save()

'''
@receiver(pre_save, sender=Profile)
def removeOldProfilePicture(sender, instance, **kwargs):
    oldpic = sender.objects.get(id=instance.id).picture.url
    if oldpic == '/media/default.jpg':
        return False
    
    newpic = instance.picture.url
    if oldpic != newpic:
        print(BASE_DIR)
        os.remove(os.path.join(ROOT_DIR, oldpic))'''