# Generated by Django 2.2.9 on 2020-07-15 18:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ruyatabirleri', '0058_rtxyorum_ruya_zaman'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rtxyorum',
            name='ruya_zaman',
        ),
    ]
