# Generated by Django 3.0.2 on 2020-08-01 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20200801_0822'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='image',
        ),
    ]
