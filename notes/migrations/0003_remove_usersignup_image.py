# Generated by Django 3.0.6 on 2021-07-11 02:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_usersignup_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usersignup',
            name='image',
        ),
    ]
