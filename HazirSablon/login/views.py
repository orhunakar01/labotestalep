from django.shortcuts import render ,redirect
from django.contrib import auth

# Create your views here.


def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,'talep/talep.html')
        else:
            return redirect('login')
    else:
        return render(request , 'login/login.html')


def logout(request):
    return render(request , 'login/logout.html')