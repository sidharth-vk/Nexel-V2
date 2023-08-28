# Generated by Django 4.2.4 on 2023-08-20 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='internships',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Name')),
                ('nop', models.IntegerField(verbose_name='No Of Positions')),
                ('location', models.CharField(max_length=250, verbose_name='Location')),
                ('tech', models.CharField(max_length=250, verbose_name='Technologies')),
                ('dis', models.CharField(max_length=350, verbose_name='One Line Description')),
                ('img', models.ImageField(upload_to='career/internship', verbose_name='Banner Image')),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
        ),
    ]
