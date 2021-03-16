from django import forms
from .models import Talep
from bootstrap_datepicker_plus import DatePickerInput , TimePickerInput , DateTimePickerInput , MonthPickerInput , \
    YearPickerInput


class TalepForm(forms.ModelForm):
    class Meta:
        model = Talep
        fields=[

            'talepEdenKisi' ,
            'talepEdildigiZaman' ,
            'talepUlasmasiGerektigiZaman' ,
            'Talep1' ,
            'talepKurumu1' ,
            'tutar1' ,
            'ihaletutar1' ,
            'Talep_2' ,
            'talepKurumu_2' ,
            'tutar_2' ,
            'ihaletutar_2' ,
            'Talep_3' ,
            'talepKurumu_3' ,
            'tutar_3' ,
            'ihaletutar_3' ,
            'Talep_4' ,
            'talepKurumu_4' ,
            'tutar_4' ,
            'ihaletutar_4' ,
            'Talep_5' ,
            'talepKurumu_5' ,
            'tutar_5' ,
            'ihaletutar_5' ,

        ]


        widgets = {
            'talepEdildigiZaman': DatePickerInput(format='%d/%m/%Y' , options={
                "format": "DD/MM/YYYY" ,  # moment date-time format
                "showClose": True ,
                "showClear": True ,
                "showTodayButton": True ,
                "locale": "tr"
            }) ,
            'talepUlasmasiGerektigiZaman': DatePickerInput(format='%d/%m/%Y' , options={
                "format": "DD/MM/YYYY" ,  # moment date-time format
                "showClose": True ,
                "showClear": True ,
                "showTodayButton": True ,
                "locale": "tr"
            }) ,
        }


class TalepForm2(forms.ModelForm):
    class Meta:
        model = Talep
        fields=[

            'talepEdenKisi' ,
            'talepEdildigiZaman' ,
            'talepUlasmasiGerektigiZaman' ,
            'Talep1' ,
            'talepKurumu1' ,
            'tutar1' ,
            'ihaletutar1' ,
            'Talep_2' ,
            'talepKurumu_2' ,
            'tutar_2' ,
            'ihaletutar_2' ,
            'Talep_3' ,
            'talepKurumu_3' ,
            'tutar_3' ,
            'ihaletutar_3' ,
            'Talep_4' ,
            'talepKurumu_4' ,
            'tutar_4' ,
            'ihaletutar_4' ,
            'Talep_5' ,
            'talepKurumu_5' ,
            'tutar_5' ,
            'ihaletutar_5' ,
            'onay0',
            'red0',
            'Aciklama0',
            'tarih0',
            'onay1',
            'red1',
            'tarih1',
            'Aciklama1',
            'onay2' ,
            'red2' ,
            'tarih2' ,
            'Aciklama2' ,
            'onay3' ,
            'red3' ,
            'tarih3' ,
            'Aciklama3' ,


        ]


        widgets = {
            'talepEdildigiZaman': DatePickerInput(format='%d/%m/%Y' , options={
                "format": "DD/MM/YYYY" ,  # moment date-time format
                "showClose": True ,
                "showClear": True ,
                "showTodayButton": True ,
                "locale": "tr"
            }) ,
            'talepUlasmasiGerektigiZaman': DatePickerInput(format='%d/%m/%Y' , options={
                "format": "DD/MM/YYYY" ,  # moment date-time format
                "showClose": True ,
                "showClear": True ,
                "showTodayButton": True ,
                "locale": "tr"
            }) ,
            'tarih1': DatePickerInput(format='%d/%m/%Y' , options={
                "format": "DD/MM/YYYY" ,  # moment date-time format
                "showClose": True ,
                "showClear": True ,
                "showTodayButton": True ,
                "locale": "tr"
            }) ,
            'tarih2': DatePickerInput(format='%d/%m/%Y' , options={
                "format": "DD/MM/YYYY" ,  # moment date-time format
                "showClose": True ,
                "showClear": True ,
                "showTodayButton": True ,
                "locale": "tr"
            }) ,
            'tarih3': DatePickerInput(format='%d/%m/%Y' , options={
                "format": "DD/MM/YYYY" ,  # moment date-time format
                "showClose": True ,
                "showClear": True ,
                "showTodayButton": True ,
                "locale": "tr"
            }) ,
        }