# Generated by Django 2.2.9 on 2020-07-13 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ruyatabirleri', '0051_remove_rtxyorum_ruya_zamanı'),
    ]

    operations = [
        migrations.AddField(
            model_name='rtxyorum',
            name='ruya_zamani',
            field=models.CharField(choices=[('1', 'Gece Yarısında'), ('2', 'Güneş doğmadan hemen önce veya hemen sonra'), ('3', 'Gün içerisinde')], help_text='Lütfen Cinsiyetinizi Belirtiniz.', max_length=1, null=True),
        ),
    ]
