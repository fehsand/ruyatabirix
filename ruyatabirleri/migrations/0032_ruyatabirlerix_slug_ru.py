# Generated by Django 2.2.9 on 2020-07-09 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ruyatabirleri', '0031_ruyatabirlerix_kelime_ar2'),
    ]

    operations = [
        migrations.AddField(
            model_name='ruyatabirlerix',
            name='slug_ru',
            field=models.SlugField(blank=True, default='', max_length=255),
        ),
    ]