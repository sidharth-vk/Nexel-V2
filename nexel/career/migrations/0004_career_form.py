# Generated by Django 4.2.4 on 2023-08-28 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0003_internship_registration'),
    ]

    operations = [
        migrations.CreateModel(
            name='career_form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Title')),
                ('nop', models.CharField(max_length=250, verbose_name='Number of Position')),
                ('location', models.CharField(max_length=250, verbose_name='Location')),
                ('jobtype', models.CharField(max_length=250, verbose_name='Job Type')),
                ('form', models.CharField(max_length=2550, verbose_name='Google form link')),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
        ),
    ]