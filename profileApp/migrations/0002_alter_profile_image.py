# Generated by Django 3.2.9 on 2021-12-04 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='profile.jpg', upload_to='profile_pics'),
        ),
    ]
