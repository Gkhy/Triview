# Generated by Django 3.2.13 on 2022-11-03 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='lat',
            field=models.CharField(default=1, max_length=80),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='lng',
            field=models.CharField(default=1, max_length=80),
            preserve_default=False,
        ),
    ]
