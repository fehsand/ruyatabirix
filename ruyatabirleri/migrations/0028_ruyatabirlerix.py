# Generated by Django 2.2.9 on 2020-07-02 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ruyatabirleri', '0027_auto_20200308_2355'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ruyatabirlerix',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kelime', models.CharField(default='', max_length=255)),
                ('slug', models.SlugField(blank=True, default='', max_length=255)),
                ('tabiri', models.TextField()),
                ('ekleme_tarihi', models.DateTimeField(auto_now_add=True)),
                ('aranma_sayisi', models.IntegerField(null=True)),
                ('kelime_en', models.CharField(max_length=200, null=True)),
                ('tabir_en', models.TextField(null=True)),
                ('altr_en_url', models.URLField(blank=True, null=True)),
                ('kelime_ar', models.CharField(max_length=200, null=True)),
                ('tabir_ar', models.TextField(null=True)),
                ('altr_ar_url', models.URLField(blank=True, null=True)),
                ('kelime_ru', models.CharField(max_length=200, null=True)),
                ('tabir_ru', models.TextField(null=True)),
                ('altr_ru_url', models.URLField(blank=True, null=True)),
                ('kelime_es', models.CharField(max_length=200, null=True)),
                ('tabir_es', models.TextField(null=True)),
                ('altr_es_url', models.URLField(blank=True, null=True)),
                ('kelime_ch', models.CharField(max_length=200, null=True)),
                ('tabir_ch', models.TextField(null=True)),
                ('altr_ch_url', models.URLField(blank=True, null=True)),
                ('kelime_in', models.CharField(max_length=200, null=True)),
                ('tabir_in', models.TextField(null=True)),
                ('altr_in_url', models.URLField(blank=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
