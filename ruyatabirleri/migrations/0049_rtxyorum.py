# Generated by Django 2.2.9 on 2020-07-13 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ruyatabirleri', '0048_ruyatabirlerix3'),
    ]

    operations = [
        migrations.CreateModel(
            name='RTXyorum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(help_text='Lütfen İsminizi Yazınız', max_length=200, verbose_name='İsminiz')),
                ('soy_isim', models.CharField(help_text='Lütfen Soyisminizi Yazınız', max_length=200, verbose_name='Soy İsminiz')),
                ('cinsiyet', models.CharField(choices=[('c', 'Cinsiyetiniz'), ('e', 'Erkek'), ('k', 'Kadın')], help_text='Lütfen Cinsiyetinizi Belirtiniz.', max_length=1, verbose_name='Cinsiyetiniz')),
                ('eposta', models.EmailField(help_text='Lütfen Eposta Adresinizi Yazınız.', max_length=200, verbose_name='Epostanız')),
                ('eposta1', models.EmailField(help_text='Lütfen Eposta Adresinizi Doğrulayınız.', max_length=200, verbose_name='Epostanız')),
                ('ruya_zamanı', models.CharField(choices=[('c', 'Cinsiyetiniz'), ('e', 'Erkek'), ('k', 'Kadın')], help_text='Lütfen Cinsiyetinizi Belirtiniz.', max_length=1, verbose_name='Cinsiyetiniz')),
                ('bilinc_alti', models.CharField(choices=[('c', 'Cinsiyetiniz'), ('e', 'Erkek'), ('k', 'Kadın')], help_text='Yatmadan önce veya gün içerisinde gördüğünüz rüya ile ilgili bir olay yaşadınız mı? veya hayal kurdunuz mu?', max_length=1, verbose_name='Rüya bilinçaltı olabilir mi?')),
                ('ruya', models.TextField(help_text='Lütfen rüyanızı basit cümlelerle ayrıntılı olarak anlatınız. Cümlelerin sonuna nokta işareti koymayı unutmayınızı.', verbose_name='Rüya')),
                ('kayit_tarihi', models.DateTimeField(auto_now_add=True, verbose_name='Kayıt Tarihi')),
            ],
        ),
    ]
