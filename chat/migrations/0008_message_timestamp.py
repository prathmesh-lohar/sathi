# Generated by Django 4.2.7 on 2023-12-21 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0007_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]