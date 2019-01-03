from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from datetime import datetime

class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

# Create your models here.
class User(AbstractUser):
    # User model que usa email ao invés do username
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    name = models.CharField(max_length=128)
    password = models.CharField(max_length=128)
    language = models.CharField(max_length=8)
    nickname = models.CharField(max_length=32)
    public_id = models.CharField(max_length=16)
    bio = models.TextField()
    # picture
    # maps has many
    # creation date
    # validated email


class Map(models.Model):
    title = models.CharField(max_length=128)
    ispublic = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="mymaps")
    # creation timestamp
    public_id = models.CharField(max_length=16, null=True, blank=True)
    friendly_url = models.CharField(max_length=128, null=True, blank=True)
    language = models.CharField(max_length=8, null=True, blank=True)
    mapjson = models.TextField(default="", null=True, blank=True)
    description = models.TextField(default="", null=True, blank=True)
    imageurl = models.CharField(max_length=512, null=True, blank=True)
    # keywords
    # views
    # number of shares

class Listing(models.Model):
    title = models.CharField(max_length=128)
    public_id = models.CharField(max_length=16)
    friendly_url = models.CharField(max_length=128)
    language = models.CharField(max_length=8)
    maps = models.ManyToManyField(Map, blank=True, related_name="maps")
    # keywords

class MapView(models.Model):
    map = models.ForeignKey(Map, related_name='mapviews', on_delete=models.SET_NULL, null=True, blank=True)
    ip = models.CharField(max_length=40)
    session = models.CharField(max_length=40, null=True, blank=True)
    created = models.DateTimeField(default=timezone.now)

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
