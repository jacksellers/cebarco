# Generated by Django 3.1.4 on 2020-12-16 12:44

from django.db import migrations, models
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_project_crop'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='crop',
        ),
        migrations.RemoveField(
            model_name='project',
            name='crop',
        ),
        migrations.AddField(
            model_name='article',
            name='cropped',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='article',
            name='image_ratio',
            field=image_cropping.fields.ImageRatioField('image', '500x500', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='image ratio'),
        ),
        migrations.AddField(
            model_name='project',
            name='cropped',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='project',
            name='image_ratio',
            field=image_cropping.fields.ImageRatioField('image', '500x500', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='image ratio'),
        ),
    ]