# Generated by Django 5.1.1 on 2024-09-21 23:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postcomment', '0003_alter_postcomment_postcomment_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postcomment',
            name='postcomment_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 22, 0, 8, 22, 17172)),
        ),
    ]
