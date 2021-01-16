from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f"{self.user.username}'s Profile"

    def save(self):
        super().save()

        image = Image.open(self.picture.path)
        if image.width > 300 or image.height > 300:
            image.thumbnail((300, 300))
            image.save(self.picture.path)