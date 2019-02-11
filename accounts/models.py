from django.contrib.auth.models import User
from django.db import models
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    introduce = models.TextField(max_length=200)
    follows = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followed_by', symmetrical=False, blank=True)


