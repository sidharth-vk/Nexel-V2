# Generated by Django 4.2.4 on 2023-08-20 15:01

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Title')),
                ('image1', models.ImageField(upload_to='blog/banner', verbose_name='Image banner')),
                ('content', ckeditor.fields.RichTextField(verbose_name='Body 1')),
                ('image2', models.ImageField(upload_to='blog/banner', verbose_name='Other Image')),
                ('content2', ckeditor.fields.RichTextField(verbose_name='Body 2')),
                ('quote', models.CharField(max_length=250, verbose_name='Quote')),
                ('date', models.DateField(auto_now=True, verbose_name='Date')),
                ('author', models.CharField(max_length=150, verbose_name='Author')),
                ('tags', models.TextField(verbose_name='Tags')),
                ('slug', models.SlugField(default='')),
            ],
        ),
    ]