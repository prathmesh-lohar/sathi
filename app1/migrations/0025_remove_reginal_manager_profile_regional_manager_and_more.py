# Generated by Django 4.2.7 on 2024-04-13 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0024_remove_reginal_manager_profile_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reginal_manager_profile',
            name='regional_manager',
        ),
        migrations.AddField(
            model_name='reginal_manager_profile',
            name='region',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]