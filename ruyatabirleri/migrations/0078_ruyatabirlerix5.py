# Generated by Django 2.2.9 on 2020-08-11 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ruyatabirleri', '0077_auto_20200811_2252'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ruyatabirlerix5',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kelime_tr', models.CharField(max_length=255)),
                ('slug_tr', models.SlugField(blank=True, max_length=255, unique=True)),
                ('tabiri_tr', models.TextField()),
                ('kelime_en', models.CharField(max_length=200)),
                ('tabiri_en', models.TextField()),
                ('altr_en_url', models.URLField(blank=True)),
                ('kelime_es', models.CharField(max_length=200)),
                ('slug_es', models.SlugField(allow_unicode=True, blank=True, max_length=255, unique=True)),
                ('tabiri_es', models.TextField()),
                ('altr_es_url', models.URLField(blank=True)),
                ('kelime_ru', models.CharField(max_length=200, null=True)),
                ('slug_ru', models.SlugField(allow_unicode=True, blank=True, max_length=255, unique=True)),
                ('tabiri_ru', models.TextField(null=True)),
                ('altr_ru_url', models.URLField(blank=True)),
                ('kelime_ar', models.CharField(max_length=200, null=True)),
                ('slug_ar', models.SlugField(allow_unicode=True, blank=True, max_length=255, unique=True)),
                ('tabiri_ar', models.TextField(null=True)),
                ('altr_ar_url', models.URLField(blank=True)),
                ('kelime_ch', models.CharField(max_length=200, null=True)),
                ('slug_ch', models.SlugField(allow_unicode=True, blank=True, max_length=255, unique=True)),
                ('tabiri_ch', models.TextField(null=True)),
                ('altr_ch_url', models.URLField(blank=True)),
                ('ekleme_tarihi', models.DateTimeField(auto_now_add=True)),
                ('guncelleme_tarihi', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
