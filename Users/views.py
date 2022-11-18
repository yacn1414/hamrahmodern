from . import models
from django.http import HttpResponse,JsonResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render,redirect

from django.contrib.auth import authenticate, login

# Create your views here.
def authlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                request.session.set_expiry(86400)
                login(request, user)
                return redirect('/account')
            else:
                messages.ERROR(request,'مشکلی در ثبت نام وجود دارد')
                return redirect('/login')
    return redirect('/login')
    # half login
def auth(request):
    
    if request.method == 'POST':
        phone = request.POST['phone']
        from requests import get
        username = "09149073874"
        password = "Rasuoli67"
        number = 50004075
        from random import randint
        code = randint(4000,5000)
        text = f"{code} کد شما در سایت همراه مدرن از دادن کد خود جز سایت hamrahmodern.com جدا خودداری کنید"
        numberTO= phone
        response = get(f"https://www.payam-resan.com/APISend.aspx?Username={username}&Password={password}&From={number}&To={numberTO}&Text={text}")
        if response:
            user = models.UserCustom.objects.create(phone=phone,code=code)
            return render(request, 'verify.html',{'phone':phone})
            
        else:
            return redirect('/register')
    else:
        return redirect("../register")

def signup(request):
    return render(request,'register.html',{})
def loginUser(request):
    return render(request,'registration/login.html',{})
def profile(request):
    if request.user.is_authenticated:
        id_use = request.user.id
        name = request.user.username
    else:
        return redirect('/login')
    user = models.UserCustom.objects.get(user__id=request.user.id)
    return render(request, 'profile.html',{"id_use":id_use,"name":name,"pro":user})

def verify(request):
    if request.method == 'POST':
        a = request.POST['code1']+request.POST['code2']+request.POST['code3']+request.POST['code4']
        if models.UserCustom.objects.get(code=a).exists():
            models.UserCustom.objects.get(code=a).delete()
        password = request.POST.get('password','')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                request.session.set_expiry(86400)
                login(request, user)
                return redirect('/account')
            else:
                messages.ERROR(request,'مشکلی در ثبت نام وجود دارد')
                return redirect('/login')