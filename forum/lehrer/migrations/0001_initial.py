# Generated by Django 4.1.7 on 2023-04-25 11:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField(validators=[django.core.validators.MinLengthValidator(15)])),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]