# Generated by Django 3.1.4 on 2021-03-07 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_auto_20210307_1415'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='article',
        ),
        migrations.RemoveField(
            model_name='image',
            name='project',
        ),
    ]
