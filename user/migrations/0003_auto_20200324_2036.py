# Generated by Django 3.0.4 on 2020-03-24 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200324_0022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user_picture',
            field=models.ImageField(default='default.jpg', upload_to='user/static/profile_pics'),
        ),
    ]
