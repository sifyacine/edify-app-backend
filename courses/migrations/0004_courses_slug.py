# Generated by Django 5.1.1 on 2024-09-23 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_alter_courses_hashtags'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, unique=True),
        ),
    ]
