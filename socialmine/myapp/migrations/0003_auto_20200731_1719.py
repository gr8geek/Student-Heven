# Generated by Django 3.0.2 on 2020-07-31 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_shirt_medal'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=100)),
                ('uname', models.CharField(max_length=60, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.DeleteModel(
            name='Shirt',
        ),
    ]
