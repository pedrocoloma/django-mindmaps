from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class UserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email',)

class UserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = User
        fields = UserChangeForm.Meta.fields
