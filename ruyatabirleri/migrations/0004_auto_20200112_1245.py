# Generated by Django 2.2.9 on 2020-01-12 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ruyatabirleri', '0003_auto_20200109_1241'),
    ]

    operations = [
        migrations.AddField(
            model_name='ruyatabirleri',
            name='ingilizce_kelime',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='ruyatabirleri',
            name='ingilizce_tabir',
            field=models.TextField(null=True),
        ),
    ]