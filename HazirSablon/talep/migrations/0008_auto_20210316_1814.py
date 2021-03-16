# Generated by Django 3.1.6 on 2021-03-16 15:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talep', '0007_auto_20210311_2136'),
    ]

    operations = [
        migrations.AddField(
            model_name='talep',
            name='Aciklama0',
            field=models.TextField(blank=True, null=True, verbose_name='Muhasebe Açıklama'),
        ),
        migrations.AddField(
            model_name='talep',
            name='onay0',
            field=models.BooleanField(default=False, verbose_name='Muhasebe Onay'),
        ),
        migrations.AddField(
            model_name='talep',
            name='red0',
            field=models.BooleanField(default=False, verbose_name='Muhasebe Red'),
        ),
        migrations.AddField(
            model_name='talep',
            name='tarih0',
            field=models.DateField(default=datetime.date.today, verbose_name='Muhasebe Talep Onay/Red Tarih'),
        ),
        migrations.AlterField(
            model_name='talep',
            name='Aciklama1',
            field=models.TextField(blank=True, null=True, verbose_name='İlgili Müdür Açıklama'),
        ),
        migrations.AlterField(
            model_name='talep',
            name='Aciklama2',
            field=models.TextField(blank=True, null=True, verbose_name='G.Müdür Açıklama'),
        ),
        migrations.AlterField(
            model_name='talep',
            name='Aciklama3',
            field=models.TextField(blank=True, null=True, verbose_name='Finans Açıklama'),
        ),
        migrations.AlterField(
            model_name='talep',
            name='onay1',
            field=models.BooleanField(default=False, verbose_name='İlgili Müdür Onay'),
        ),
        migrations.AlterField(
            model_name='talep',
            name='onay2',
            field=models.BooleanField(default=False, verbose_name='G.Müdür  Onay'),
        ),
        migrations.AlterField(
            model_name='talep',
            name='onay3',
            field=models.BooleanField(default=False, verbose_name='Finans Onay'),
        ),
        migrations.AlterField(
            model_name='talep',
            name='red1',
            field=models.BooleanField(default=False, verbose_name='İlgili Müdür Red '),
        ),
        migrations.AlterField(
            model_name='talep',
            name='red2',
            field=models.BooleanField(default=False, verbose_name='G.Müdür  Red '),
        ),
        migrations.AlterField(
            model_name='talep',
            name='red3',
            field=models.BooleanField(default=False, verbose_name='Finans Red '),
        ),
        migrations.AlterField(
            model_name='talep',
            name='tarih1',
            field=models.DateField(default=datetime.date.today, verbose_name='İlgili Müdür Onay/Red Tarih'),
        ),
        migrations.AlterField(
            model_name='talep',
            name='tarih2',
            field=models.DateField(default=datetime.date.today, verbose_name='G.Müdür  Onay/Red Tarih'),
        ),
        migrations.AlterField(
            model_name='talep',
            name='tarih3',
            field=models.DateField(default=datetime.date.today, verbose_name='Finans Onay/Red Tarih'),
        ),
    ]
