# Generated by Django 2.2.9 on 2020-07-11 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ruyatabirleri', '0041_ruyatabirlerix2_kelime_ru'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ruyatabirlerix2',
            name='altr_ru_url',
        ),
        migrations.RemoveField(
            model_name='ruyatabirlerix2',
            name='kelime_ru',
        ),
        migrations.RemoveField(
            model_name='ruyatabirlerix2',
            name='slug_ru',
        ),
        migrations.RemoveField(
            model_name='ruyatabirlerix2',
            name='tabiri_ru',
        ),
    ]