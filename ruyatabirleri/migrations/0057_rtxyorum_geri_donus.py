# Generated by Django 2.2.9 on 2020-07-14 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ruyatabirleri', '0056_auto_20200714_0026'),
    ]

    operations = [
        migrations.AddField(
            model_name='rtxyorum',
            name='geri_donus',
            field=models.BooleanField(default=False, help_text='Cevap yazılan rüya tabirleri true yapılacak'),
        ),
    ]
