# Generated by Django 3.1.4 on 2021-02-23 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0014_auto_20210223_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='songfile',
            name='file_size',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
    ]