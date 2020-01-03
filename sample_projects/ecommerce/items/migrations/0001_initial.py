# Generated by Django 2.2.7 on 2020-01-03 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('image', models.URLField(blank=True, max_length=256, null=True)),
                ('price', models.FloatField()),
            ],
        ),
    ]
