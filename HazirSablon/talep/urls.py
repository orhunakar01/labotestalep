from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns=[
    url(r'^update/(?P<pk>\d+)$', views.talep_update, name='talep_update'),
    url(r'^detay/(?P<pk>\d+)$', views.talep_detail, name='talep_detail'),
    url(r'^delete/(?P<pk>\d+)$' , views.talep_delete , name='talep_delete') ,
    path("talepekle/",views.talep_ekle,name='talep_ekle'),

    url('onayli/' , views.onayli , name='onayli') ,
    url('onaysiz/' , views.onaysiz , name='onaysiz') ,
    url('beklemede/' , views.beklemede , name='beklemede') ,
    path('', views.talep_views, name='talep_views'),

]