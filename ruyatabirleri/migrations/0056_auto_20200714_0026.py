# Generated by Django 2.2.9 on 2020-07-13 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ruyatabirleri', '0055_rtxyorum_kayit_tarihi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rtxyorum',
            name='bilinc_alti',
            field=models.CharField(help_text='Yatmadan önce veya gün içerisinde gördüğünüz rüya ile ilgili bir olay yaşadınız mı? veya hayal kurdunuz mu?', max_length=200),
        ),
        migrations.AlterField(
            model_name='rtxyorum',
            name='cinsiyet',
            field=models.CharField(help_text='Lütfen Cinsiyetinizi Belirtiniz.', max_length=10),
        ),
        migrations.AlterField(
            model_name='rtxyorum',
            name='ruya_zamani',
            field=models.CharField(help_text='Lütfen rüyayı ne zaman gördüğünüzü belirtiniz.', max_length=200, null=True),
        ),
    ]
