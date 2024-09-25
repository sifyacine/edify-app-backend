# Generated by Django 5.1.1 on 2024-09-22 21:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hashtag', '0001_initial'),
        ('members', '0003_alter_member_general_rating_alter_member_num_courses_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=30)),
                ('course_title', models.CharField(max_length=50)),
                ('course_desc', models.TextField(max_length=800)),
                ('course_video_intro', models.FileField(upload_to='course/%y/%m/%d')),
                ('course_img_video', models.ImageField(upload_to='course/images/%y/%m/%d')),
                ('course_video_number', models.IntegerField()),
                ('course_rating', models.IntegerField(default=0)),
                ('course_time', models.DateTimeField(auto_now_add=True)),
                ('hashtags', models.ManyToManyField(related_name='courses', to='hashtag.hashtag')),
                ('member', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='members.member')),
            ],
        ),
    ]
