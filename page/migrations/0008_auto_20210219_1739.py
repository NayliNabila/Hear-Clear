# Generated by Django 3.1.4 on 2021-02-19 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0007_songfile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='songfile',
            name='filetype',
            field=models.FileField(upload_to='songs'),
        ),
    ]
