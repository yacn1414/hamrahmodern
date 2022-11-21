from . import models
from django.http import HttpResponse,JsonResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from main.models import sabad,BrandMobile,jamsabad,category,Product
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
    
def auth(request):
    
    if request.method == 'POST':

        
        import requests
        from random import randint
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
        user = models.UserCustom.objects.create(phone=phone,code=code)
        if user:
            return render(request, 'verify.html',{'phone':phone})
            
        
        
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
        if models.UserCustom.objects.filter(code=a).exists():
            ab = models.UserCustom.objects.get(code=a)
            request.session['verify'] = ab.phone
            ab.code = ""
            ab.save()

            return render(request, 'welcome.html')
        else:
            return redirect('/register')
def complete(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            id_use = request.user.id
            name = request.user.username
            sabad220 = len(sabad.objects.filter(id_user=request.user.id))
        else:
            id_use = 0
            name = None
            sabad220 = 0
        ABrands = BrandMobile.objects.all()
        jamsaba = jamsabad.objects.all()
        product_all = Product.objects.all()
        
        categor = category.objects.all()
        saba = sabad.objects.all()
        return render(request, 'profile-additional-info1.html',{"allp":product_all,"name":name,"id_use":id_use,
        "category":categor,
        
        "sabad":sabad220,
        
        "saba":saba,"Brands":ABrands,"jamsabad":jamsaba})
        
    else:
        return redirect('../')
def Done(request):
    if request.method == "POST":
        moduser = User.objects.create_user(username=request.POST['name'],email=request.POST['email'],password = request.POST['password'])
        upd = models.UserCustom.objects.filter(phone=request.session['verify']).update(user=moduser)
        if udp is not None:
            if user.is_active:
                request.session.set_expiry(86400)
                login(request, user)
                return redirect('/account')
            else:
                messages.ERROR(request,'مشکلی در ثبت نام وجود دارد')
                return redirect('/login')
        return render(request, 'profile.html',{"id_use":request.user.id})
    else:
        return redirect('/')