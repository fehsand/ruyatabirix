# Generated by Django 2.2.9 on 2020-01-14 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ruyatabirleri', '0007_delete_ruyatabirleri1'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Ruyatabirleri2',
        ),
        migrations.AddField(
            model_name='ruyatabirleri',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
