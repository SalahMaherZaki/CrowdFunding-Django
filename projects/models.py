from django.db import models
from django.contrib.auth.models import User
from django.core.validators import *


class Category(models.Model):
    category_name = models.CharField(max_length=20)
    def __str__(self):
        return self.category_name


class Tag (models.Model):
    tag_name = models.CharField(max_length=10)

    def __str__(self):
        return self.tag_name



class Projects (models.Model):
    project_title = models.CharField(max_length=40)
    project_details = models.TextField(default=' ')
    total_donation = models.IntegerField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag , related_name='tags')
    category = models.ManyToManyField(Category , related_name='categories')


    def __str__(self):
        return self.project_title



class Images (models.Model):
    img = models.ImageField(upload_to="HomePage/static/image/")
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, null=False)

class Comment (models.Model):
    
    project_id = models.ForeignKey(Projects, on_delete=models.CASCADE)
    comment_content = models.TextField(default=' ')

    def __str__(self):
        return f"comment by {user_id.user_fname} on {project_id.project_title}"


class Donation (models.Model):
    project_id = models.ForeignKey(Projects, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    donation_amount = models.IntegerField()

    def __str__(self):
        return f"donation by {user_id.user_fname} on {project_id.project_title}"


class Rate (models.Model):
    project_id = models.ForeignKey(Projects, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    rate_content = models.TextField(default=' ')
    rate_number = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)])


class FeaturedProject (models.Model):
    proj = models.ForeignKey(Projects, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.proj.title)


class Report (models.Model):
  
    project_id = models.ForeignKey(Projects, on_delete=models.CASCADE)
    report_content = models.TextField(default=' ')
