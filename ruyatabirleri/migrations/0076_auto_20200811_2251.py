# Generated by Django 2.2.9 on 2020-08-11 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ruyatabirleri', '0075_delete_ruyatabirlerix5'),
    ]

    operations = [
        migrations.AddField(
            model_name='ruyatabirlerix3',
            name='altr_ar_url',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='ruyatabirlerix3',
            name='altr_ch_url',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='ruyatabirlerix3',
            name='kelime_ar',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='ruyatabirlerix3',
            name='kelime_ch',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='ruyatabirlerix3',
            name='slug_ar',
            field=models.SlugField(allow_unicode=True, blank=True, max_length=255, unique=True),
        ),
        migrations.AddField(
            model_name='ruyatabirlerix3',
            name='slug_ch',
            field=models.SlugField(allow_unicode=True, blank=True, max_length=255, unique=True),
        ),
        migrations.AddField(
            model_name='ruyatabirlerix3',
            name='tabiri_ar',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='ruyatabirlerix3',
            name='tabiri_ch',
            field=models.TextField(null=True),
        ),
    ]
