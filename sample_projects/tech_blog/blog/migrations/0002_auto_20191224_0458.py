# Generated by Django 2.2.7 on 2019-12-24 04:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 24, 4, 58, 27, 385133, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 24, 4, 58, 27, 384727, tzinfo=utc)),
        ),
    ]
