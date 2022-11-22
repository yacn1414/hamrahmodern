from . import models
from django.http import HttpResponse,JsonResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from main.models import sabad,BrandMobile,jamsabad,category,Product
from django.contrib.auth import authenticate, login
from Users.models import UserCustom
from main.models import sabad,category,BrandMobile
# Create your views here.
def sefaresh(request):
    if request.user.is_authenticated:
        id_use = request.user.id
        name = request.user.username
        user = UserCustom.objects.get(user__id=id_use)
        sab = sabad.objects.filter(id_user=id_use).count()
        product_all = Product.objects.all()
        ABrands = BrandMobile.objects.all()
        categories = category.objects.all()
        saba = sabad.objects.all()

        
        return render(request, 'profile-order.html',{"user":user,"sabad":sab,"saba":saba,"category":categories,"allp":product_all,"id_use":id_use,"name":name,"Brands":ABrands})
        
def authlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'profile.html')
            
        else:
            return redirect('/login')
            # No backend authenticated the credentials
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
        user = UserCustom.objects.get(user__id=id_use)
        sab = sabad.objects.filter(id_user=id_use).count()
        product_all = Product.objects.all()
        ABrands = BrandMobile.objects.all()
        categories = category.objects.all()
        saba = sabad.objects.all()

        
        return render(request, 'profile.html',{"user":user,"sabad":sab,"saba":saba,"category":categories,"allp":product_all,"id_use":id_use,"name":name,"Brands":ABrands})
        
    else:
        return redirect('/login')

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
            if upd.is_active:
                request.session.set_expiry(86400)
                login(request, user)
                return redirect('/account')
            else:
                messages.ERROR(request,'مشکلی در ثبت نام وجود دارد')
                return redirect('/login')
        return render(request, 'profile.html',{"id_use":request.user.id})
    else:
        return redirect('/')