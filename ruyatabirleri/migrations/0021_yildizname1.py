# Generated by Django 2.2.9 on 2020-02-22 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ruyatabirleri', '0020_yildizname'),
    ]

    operations = [
        migrations.CreateModel(
            name='yildizname1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=200)),
                ('anne_ismi', models.CharField(max_length=200)),
                ('cinsiyet', models.CharField(max_length=200)),
            ],
        ),
    ]
