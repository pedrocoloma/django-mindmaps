from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

# Create your models here.
# class User(models.Model):
#     name = models.CharField(max_length=128)
#     email = models.CharField(max_length=128)
#     password = models.CharField(max_length=128)
#     language = models.CharField(max_length=8)
#     nickname = models.CharField(max_length=32)
#     public_id = models.CharField(max_length=16)
#     bio = models.TextField()
    # picture
    # maps has many
    # creation date
    # validated email

class CustomUserManager(UserManager):
    pass

class CustomUser(AbstractUser):
    objects = CustomUserManager()

    name = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    password = models.CharField(max_length=128)
    language = models.CharField(max_length=8)
    nickname = models.CharField(max_length=32)
    public_id = models.CharField(max_length=16)
    bio = models.TextField()
    # has mapas    maps = models.ManyToManyField(Map, blank=True, related_name="maps")
    # follows listings


class Map(models.Model):
    title = models.CharField(max_length=128)
    ispublic = models.BooleanField(default=False)
    author = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name="mymaps")
    # creation timestamp
    public_id = models.CharField(max_length=16)
    friendly_url = models.CharField(max_length=128)
    language = models.CharField(max_length=8)
    # keywords
    # views
    # number of shares

# class UsersMaps(models.Model):
#     user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
#     maps = models.ManyToManyField(Map, blank=True, related_name="maps")

class Listing(models.Model):
    title = models.CharField(max_length=128)
    public_id = models.CharField(max_length=16)
    friendly_url = models.CharField(max_length=128)
    language = models.CharField(max_length=8)
    maps = models.ManyToManyField(Map, blank=True, related_name="maps")
    # keywords

"""
Map
    id, title, public, author, timestamp, public_id, friemdly_url, language, keywords
User
    id, public_id, name, email, password, language, nickname, bio, picture, maps
Reads
    id, user_id, was_user_registered, timestamp
Trends
Featured
"""
