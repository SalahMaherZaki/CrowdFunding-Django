# Generated by Django 3.0.4 on 2020-03-21 20:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='project',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='project',
        ),
        migrations.AddField(
            model_name='projects',
            name='category',
            field=models.ManyToManyField(related_name='categories', to='projects.Category'),
        ),
        migrations.AddField(
            model_name='projects',
            name='tag',
            field=models.ManyToManyField(related_name='tags', to='projects.Tag'),
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_content', models.TextField(default=' ')),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Projects')),
            ],
        ),
    ]
