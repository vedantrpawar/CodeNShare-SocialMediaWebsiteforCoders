# Generated by Django 3.0.5 on 2021-05-01 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_user_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(null=True, upload_to='home/static/home/images/profile_pics/', verbose_name='Image'),
        ),
    ]
