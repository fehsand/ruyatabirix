# Generated by Django 2.2.9 on 2020-07-11 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ruyatabirleri', '0043_delete_ruyatabirlerix2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ruyatabirlerix2',
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
                ('ekleme_tarihi', models.DateTimeField(auto_now_add=True)),
                ('guncelleme_tarihi', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
