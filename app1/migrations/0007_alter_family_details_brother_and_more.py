# Generated by Django 4.2.4 on 2023-11-07 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_document_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='family_details',
            name='brother',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='family_details',
            name='native_place',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='family_details',
            name='relatives',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='family_details',
            name='sister',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='about_me',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
