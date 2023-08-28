# Generated by Django 4.2.4 on 2023-08-22 05:41

import certificate.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificate', '0006_remove_certificate_offerletter_for_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='offerletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.CharField(max_length=250, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Name')),
                ('email', models.CharField(max_length=250, verbose_name='Email')),
                ('offerletter_for', models.CharField(max_length=250, verbose_name='Offer Letter For')),
                ('image', models.ImageField(upload_to=certificate.models.custom_upload_offerletter, verbose_name='Certificate image')),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
        ),
    ]