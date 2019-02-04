from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .form import UserRegisterForm

class UserProfile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profile/1.png', upload_to='profile')
    
    def __str__(self):
        return self.username.username
    

@receiver(post_save, sender=User)
def create_profile(sender,instance, **kwargs):
    if kwargs['created']:
        UserProfile.objects.create(username=instance)

@receiver(post_save, sender=User)
def save_profile(sender,instance, **kwargs):
        instance.userprofile.save()

