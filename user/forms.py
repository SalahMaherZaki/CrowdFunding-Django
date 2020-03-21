from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class userUpdateForm(forms.ModelForm):
    class Meta:
         model = User
         fields = ['username', 'first_name', 'last_name']


class profileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user_picture', 'birth_date', 'country', 'facebook_url']
