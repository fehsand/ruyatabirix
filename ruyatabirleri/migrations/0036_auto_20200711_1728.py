# Generated by Django 2.2.9 on 2020-07-11 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ruyatabirleri', '0035_auto_20200710_1729'),
    ]

    operations = [
        migrations.AddField(
            model_name='ruyatabirlerix2',
            name='kelime_ru',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='ruyatabirlerix2',
            name='slug_ru',
            field=models.SlugField(allow_unicode=True, blank=True, max_length=255, unique=True),
        ),
        migrations.AddField(
            model_name='ruyatabirlerix2',
            name='tabiri_ru',
            field=models.TextField(null=True),
        ),
    ]
