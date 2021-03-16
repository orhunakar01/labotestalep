from django.contrib.auth import login
from django.shortcuts import render , redirect , get_object_or_404
from .forms import TalepForm , TalepForm2
from .models import Talep
from django.db.models import Q
from django.contrib.auth.decorators import login_required , permission_required


@login_required(login_url=login)
def talep_views(request):
    if request.user.is_staff or request.user.is_superuser:
        listele = Talep.objects.all().order_by('-pk')
    else:
        listele = Talep.objects.filter(talepEdenKisi=request.user).order_by('-pk')
    return render(request,'talep/talep.html',{'listele':listele})


@login_required(login_url=login)
def talep_detail(request , pk):
    liste = get_object_or_404(Talep , id=pk)
    context = {'liste': liste}
    return render(request , 'talep/create.html' , context)


@login_required(login_url=login)
@permission_required('talep.add_talep',login_url=talep_views)
def talep_ekle(request):
    create=TalepForm(request.POST or None)
    context={'create':create}
    if request.method=="POST":
        if create.is_valid():
            create.save()
            return redirect('talep_views')
    return render(request,'talep/create.html',context)



@login_required(login_url=login)
@permission_required('talep.change_talep',login_url=talep_views)
def talep_update(request , pk):
    liste = get_object_or_404(Talep , id=pk)
    create = TalepForm2(request.POST or None , request.FILES or None , instance=liste)
    if create.is_valid():
        create.save()
        return redirect('talep_views')
    context = {'create': create}
    return render(request , 'talep/create.html' , context)


@login_required(login_url=login)
@permission_required('talep.delete_talep',login_url=talep_views)
def talep_delete(request , pk):
    liste = Talep.objects.get(id=pk)
    #   if User.groups.name('Yetkili'):
    liste.delete()
    context = {'liste': liste}
    return redirect('talep_views')


@login_required(login_url=login)
def onayli(request):
    if request.user.is_staff or request.user.is_superuser:
        listele = Talep.objects.filter(onay1=True,onay2=True,onay3=True).order_by('-pk')
    else:
        listele = Talep.objects.filter(talepEdenKisi=request.user,onay1=True,onay2=True,onay3=True).order_by('-pk')
    return render(request,'talep/talep.html',{'listele': listele})


@login_required(login_url=login)
def onaysiz(request):
    if request.user.is_staff or request.user.is_superuser:
        listele = Talep.objects.filter(Q(red1=True) | Q(red2=True) | Q(red3=True))
    else:
        listele = Talep.objects.filter(Q(talepEdenKisi=request.user) | Q(red1=True) | Q(red2=True) | Q(red3=True))
    return render(request,'talep/talep.html',{'listele': listele})


@login_required(login_url=login)
def beklemede(request):
    if request.user.is_staff or request.user.is_superuser:
        listele = Talep.objects.filter(Q(red1=False,onay1=False) | Q(red2=False,onay2=False) | Q(red3=False,onay3=False))
    else:
        listele = Talep.objects.filter(Q(talepEdenKisi=request.user,red1=False,onay1=False) | Q(red2=False,onay2=False) | Q(red3=False,onay3=False))
    return render(request,'talep/talep.html',{'listele': listele})