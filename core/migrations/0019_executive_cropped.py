# Generated by Django 3.1.4 on 2020-12-21 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_executive_image_ratio'),
    ]

    operations = [
        migrations.AddField(
            model_name='executive',
            name='cropped',
            field=models.BooleanField(default=False),
        ),
    ]