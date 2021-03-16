from datetime import date
from urllib import request

from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.context_processors import auth
from django.contrib.auth.models import User
from django.db import models



class Talep(models.Model):
    talepEdenKisi=models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='Talep Eden Kişi',blank=True,null=True)
    #talepEdenKisi = models.CharField(verbose_name='Talep Eden' , max_length=100,default='')
    talepEdildigiZaman = models.DateTimeField(verbose_name='Talep Edildiği Zaman')
    talepUlasmasiGerektigiZaman = models.DateTimeField(verbose_name='Talep Bitiş Süresi')

    Talep1 = models.CharField(max_length=200 , verbose_name='Talep-1')
    talepKurumu1 = models.CharField(max_length=120 , verbose_name='Talebin Yapılacağı Kurum')
    tutar1 = models.FloatField(verbose_name='Talep Yaklasık Tutarı')
    ihaletutar1 = models.FloatField(verbose_name='Firma Yaklasık Kalan Tutar' , null=True , blank=True)

    Talep_2 = models.CharField(max_length=200 , null=True , blank=True , verbose_name='Talep-2')
    talepKurumu_2 = models.CharField(max_length=120 , verbose_name='Talebin Yapılacağı Kurum2' , null=True ,
                                   blank=True)
    tutar_2 = models.FloatField(verbose_name='Talep Yaklasık Tutarı2' , null=True , blank=True)
    ihaletutar_2 = models.FloatField(verbose_name='Firma Yaklasık Kalan Tutar2' , null=True , blank=True)

    Talep_3 = models.CharField(max_length=200 , null=True , blank=True , verbose_name='Talep-3')
    talepKurumu_3 = models.CharField(max_length=120 , verbose_name='Talebin Yapılacağı Kurum3' , null=True ,
                                     blank=True)
    tutar_3 = models.FloatField(verbose_name='Talep Yaklasık Tutarı3' , null=True , blank=True)
    ihaletutar_3 = models.FloatField(verbose_name='Firma Yaklasık Kalan Tutar3' , null=True , blank=True)

    Talep_4 = models.CharField(max_length=200 , null=True , blank=True , verbose_name='Talep-4')
    talepKurumu_4 = models.CharField(max_length=120 , verbose_name='Talebin Yapılacağı Kurum4' , null=True ,
                                     blank=True)
    tutar_4 = models.FloatField(verbose_name='Talep Yaklasık Tutarı4' , null=True , blank=True)
    ihaletutar_4 = models.FloatField(verbose_name='Firma Yaklasık Kalan Tutar4' , null=True , blank=True)

    Talep_5 = models.CharField(max_length=200 , null=True , blank=True , verbose_name='Talep-5')
    talepKurumu_5 = models.CharField(max_length=120 , verbose_name='Talebin Yapılacağı Kurum5' , null=True ,
                                     blank=True)
    tutar_5 = models.FloatField(verbose_name='Talep Yaklasık Tutarı5' , null=True , blank=True)
    ihaletutar_5 = models.FloatField(verbose_name='Firma Yaklasık Kalan Tutar5' , null=True , blank=True)

    onay0=models.BooleanField(default=False,verbose_name='Muhasebe Onay')
    red0=models.BooleanField(default=False,verbose_name='Muhasebe Red')
    tarih0=models.DateField(default=date.today , verbose_name='Muhasebe Talep Onay/Red Tarih')
    Aciklama0=models.TextField(blank=True , null=True,verbose_name='Muhasebe Açıklama')

    onay1     = models.BooleanField(default=False , verbose_name='İlgili Müdür Onay')
    red1      = models.BooleanField(default=False , verbose_name='İlgili Müdür Red ')
    tarih1          = models.DateField(default=date.today , verbose_name='İlgili Müdür Onay/Red Tarih')
    Aciklama1   = models.TextField(blank=True , null=True,verbose_name='İlgili Müdür Açıklama')

    onay2 = models.BooleanField(default=False , verbose_name='G.Müdür  Onay')
    red2= models.BooleanField(default=False , verbose_name='G.Müdür  Red ')
    tarih2 = models.DateField(default=date.today , verbose_name='G.Müdür  Onay/Red Tarih')
    Aciklama2 = models.TextField(blank=True , null=True,verbose_name='G.Müdür Açıklama')

    onay3 = models.BooleanField(default=False , verbose_name='Finans Onay')
    red3= models.BooleanField(default=False , verbose_name='Finans Red ')
    tarih3 = models.DateField(default=date.today , verbose_name='Finans Onay/Red Tarih')
    Aciklama3= models.TextField(blank=True , null=True,verbose_name='Finans Açıklama')

    def __str__(self):
        return self.talepEdenKisi

    def publish(self):
        self.talepEdildigiZaman = date.today()
        self.save()
