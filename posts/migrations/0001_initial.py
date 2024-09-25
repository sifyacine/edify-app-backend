# Generated by Django 5.0.7 on 2024-09-21 22:35

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
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.TextField(max_length=800)),
                ('post_likes', models.IntegerField(default=0)),
                ('post_comments', models.IntegerField(default=0)),
                ('post_time', models.DateTimeField(auto_now_add=True)),
                ('hashtags', models.ManyToManyField(related_name='posts', to='hashtag.hashtag')),
                ('member', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='members.member')),
            ],
        ),
        migrations.CreateModel(
            name='PostImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='post_images/%y/%m/%d')),
                ('postimage_time', models.DateTimeField(auto_now_add=True)),
                ('member', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='members.member')),
                ('post', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='posts.post')),
            ],
        ),
    ]
