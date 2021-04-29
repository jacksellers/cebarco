# Generated by Django 3.1.4 on 2020-12-16 12:29

from django.db import migrations
import image_cropping.fields
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_article_cropping'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='cropping',
        ),
        migrations.AddField(
            model_name='article',
            name='crop',
            field=image_cropping.fields.ImageRatioField('image', '500x500', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='crop'),
        ),
        migrations.AlterField(
            model_name='article',
            name='text',
            field=markdownx.models.MarkdownxField(help_text='\n                You can use\n                <a href="https://www.markdownguide.org/cheat-sheet/" \n                target="_blank">\n                markdown</a> here to format the text \n            '),
        ),
        migrations.AlterField(
            model_name='project',
            name='text',
            field=markdownx.models.MarkdownxField(blank=True, help_text='\n                You can use\n                <a href="https://www.markdownguide.org/cheat-sheet/" \n                target="_blank">\n                markdown</a> here to format the text \n            '),
        ),
    ]