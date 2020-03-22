from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from projects.models import Projects


class userUpdateForm(forms.ModelForm):
    class Meta:
         model = User
         fields = ['username', 'first_name', 'last_name']


class profileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user_picture', 'birth_date', 'country', 'facebook_url']




class projectUpdateForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ['project_title', 'project_details', 'total_donation', 'start_time', 'end_time']

