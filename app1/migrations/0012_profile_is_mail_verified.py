# Generated by Django 4.2.4 on 2023-08-10 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0011_alter_media_dp'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_mail_verified',
            field=models.BooleanField(default=False),
        ),
    ]
