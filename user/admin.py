from django.contrib import admin
from .models import Profile, UserPhone
from .forms import userUpdateForm, profileUpdateForm
# Register your models here.

admin.site.register(Profile)
admin.site.register(UserPhone)
# admin.site.register(userUpdateForm)



