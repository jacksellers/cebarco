# Generated by Django 3.1.3 on 2020-12-07 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_auto_20201207_1415'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
                ('team', models.BooleanField()),
            ],
            options={
                'verbose_name_plural': 'entities',
            },
        ),
        migrations.DeleteModel(
            name='Organisation',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
