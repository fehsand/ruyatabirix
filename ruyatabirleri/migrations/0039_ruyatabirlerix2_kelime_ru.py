# Generated by Django 2.2.9 on 2020-07-11 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ruyatabirleri', '0038_remove_ruyatabirlerix2_kelime_ru'),
    ]

    operations = [
        migrations.AddField(
            model_name='ruyatabirlerix2',
            name='kelime_ru',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
