# Generated by Django 3.0.5 on 2021-04-22 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20210422_1221'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='dislikes',
        ),
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
    ]
