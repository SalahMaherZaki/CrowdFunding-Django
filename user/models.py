from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_picture = models.ImageField(upload_to='profile_pics',default='default.jpg')
    phoneNum = models.CharField(max_length=11)
    birth_date = models.DateField(null=True , blank=True , auto_now=False, auto_now_add=False)
    country = models.CharField(max_length=20, null=True, blank=True)
    fb_url_regex = RegexValidator(regex=r'.+www.facebook.com\/[^\/]+$')
    facebook_url = models.URLField(null=True, blank=True, max_length=300, validators=[fb_url_regex])

    def __str__(self):
        return f'{self.user.username} Profile'

    def delete(self, using=None, keep_parents=False):
        return self.user.delete()


#class UserPhone(models.Model):
#    phone_regex = RegexValidator(regex=r'^[+-]?[0-9]+$')
#   phone = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, validators=[phone_regex], max_length=11)
#
#   def __str__(self):
#      return f'{self.phone}'
