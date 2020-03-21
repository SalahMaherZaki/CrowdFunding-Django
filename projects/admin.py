from django.contrib import admin
from .models import Category, Projects, Tag, Images
# Register your models here.

admin.site.register(Projects)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Images)
