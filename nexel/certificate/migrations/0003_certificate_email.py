# Generated by Django 4.2.4 on 2023-08-21 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificate', '0002_certificate_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='email',
            field=models.CharField(default=1, max_length=250, verbose_name='Email'),
            preserve_default=False,
        ),
    ]