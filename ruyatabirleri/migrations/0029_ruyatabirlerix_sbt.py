# Generated by Django 2.2.9 on 2020-07-02 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ruyatabirleri', '0028_ruyatabirlerix'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ruyatabirlerix_sbt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kelime', models.CharField(default='', max_length=255)),
                ('slug', models.SlugField(blank=True, default='', max_length=255)),
                ('ekleme_tarihi', models.DateTimeField(auto_now_add=True)),
                ('altr_en_url', models.URLField(blank=True, null=True)),
                ('altr_ar_url', models.URLField(blank=True, null=True)),
                ('altr_ru_url', models.URLField(blank=True, null=True)),
                ('altr_es_url', models.URLField(blank=True, null=True)),
                ('altr_ch_url', models.URLField(blank=True, null=True)),
                ('altr_in_url', models.URLField(blank=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
