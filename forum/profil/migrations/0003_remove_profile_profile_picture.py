# Generated by Django 4.1.7 on 2023-04-26 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0002_profile_profile_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='profile_picture',
        ),
    ]
