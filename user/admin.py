from django.contrib import admin
from .models import Profile
from .forms import userUpdateForm, profileUpdateForm
# Register your models here.

admin.site.register(Profile)



