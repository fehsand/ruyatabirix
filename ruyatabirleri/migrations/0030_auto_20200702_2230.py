# Generated by Django 2.2.9 on 2020-07-02 19:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ruyatabirleri', '0029_ruyatabirlerix_sbt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ruyatabirlerix',
            name='altr_in_url',
        ),
        migrations.RemoveField(
            model_name='ruyatabirlerix',
            name='kelime_in',
        ),
        migrations.RemoveField(
            model_name='ruyatabirlerix',
            name='tabir_in',
        ),
        migrations.RemoveField(
            model_name='ruyatabirlerix_sbt',
            name='altr_in_url',
        ),
    ]
