# Generated by Django 4.2.7 on 2023-12-31 19:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app1', '0012_alter_family_details_father_education_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='follow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ufrom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ufrom', to=settings.AUTH_USER_MODEL)),
                ('uto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uto', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
