# Generated by Django 3.1.4 on 2021-02-25 20:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0020_auto_20210225_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='date_added',
            field=models.DateTimeField(default=87),
        ),
    ]
