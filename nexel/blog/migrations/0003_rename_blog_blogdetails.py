# Generated by Django 4.2.4 on 2023-08-20 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blog_slug'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='blog',
            new_name='blogDetails',
        ),
    ]
