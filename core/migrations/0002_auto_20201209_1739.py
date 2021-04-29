# Generated by Django 3.1.4 on 2020-12-09 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='contract_currency',
        ),
        migrations.AlterField(
            model_name='project',
            name='contract_price',
            field=models.IntegerField(default=0, help_text='\n            US dollars\n        '),
            preserve_default=False,
        ),
    ]