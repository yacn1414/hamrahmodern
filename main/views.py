
from django.contrib import messages
from django.shortcuts import render,redirect,HttpResponse
from . import models
from Users.models import UserCustom
# Create your views here.

def main(request):
    Offrs = []
    if request.user.is_authenticated:
        id_use = request.user.id
        name = request.user.username
    else:
        id_use = 0
        name = None
    ABrands = models.BrandMobile.objects.all()
    jamsabad = models.jamsabad.objects.all()
    
    
    category = models.category.objects.all()
    product_all = models.Product.objects.all()
    if request.user.is_authenticated:
        
        sabad = len(models.sabad.objects.filter(id_user=request.user.id))
        ino = len(models.interest.objects.filter(id_user=request.user.id))

    else:
        sabad = 0
        ino = 0
    saba = models.sabad.objects.all()
    
    
    for e in models.Product.objects.all():
        if e.price_offer != None:
            
            
            Offrs += models.Product.objects.filter(name= e)

    
    return render(request,
    "main.html"
    ,
    {"name":name,"id_use":id_use,"ofpr":Offrs,
    "category":category,"allp":product_all,
    
    "ino":ino,"sabad":sabad,
    "saba":saba,"Brands":ABrands,"jamsabad":jamsabad}
    )
def sellers(request):
    return HttpResponse("به زودی ...")


def search(request):
    if request.method == "POST":
        search = request.POST['search_cahr']
        context = models.Product.objects.filter(name__contains=search)
        T = len(context)
    else:
        context = None
        search = ''
        T = 0
    if request.user.is_authenticated:
        sabadcount = models.sabad.objects.count()
        ino = models.interest.objects.count()
        saba = models.sabad.objects.all()
        id_use = request.user.id
        name = request.user.username
        allp = models.Product.objects.all()
    else:
        sabadcount = 0
        ino = 0
        saba = None
        id_use = 0
        name = None
        allp = None
    return render(request, 'opiran.html',{"context":context,"search":search,'T':T,
    "ino":ino,"sabad":sabadcount,"saba":saba,"id_use":id_use,"name":name,"allp":allp,
    })


def sabad(request,id=0):


    if request.user.username:
        name = request.user.username
    else:
        name = None

    if request.method == "POST":
          
        if request.user.is_authenticated:
            if models.sabad.objects.filter(id_user=request.user.id,id_pro=id).exists():
                return redirect("../")
            else:
                t = request.POST['T']
                color = request.POST['color']
                id_pro = request.POST['id']
                id_user = request.POST['id_user']
                p = request.POST['p']
                p2 = request.POST['p2']
                models.sabad.objects.create(color=color,id_user=id_user,id_pro=id_pro,T=t,p=p,p2=p2)
                return redirect("/cart")
        else:
            return redirect('/')
    id_use = 0
       
    if request.user.is_authenticated:
        id_use = request.user.id
        name = request.user.username
        
    #################################################################################
    sabad = models.sabad.objects.filter(id_user=id_use).count()
    
    saba = models.sabad.objects.all()
    category = models.category.objects.all()
    product_all = models.Product.objects.all()
    ABrands = models.BrandMobile.objects.all()
    if sabad == 0 :
        return render(request,
            "cart.html",{
        "ino":ino,"sabad":sabad,"saba":saba,"category":category,"allp":product_all,"id_use":id_use,"name":name,"Brands":ABrands
            })
    else:
        return render(request,
            "sabad.html",{
        "sabad":sabad,"saba":saba,"category":category,"allp":product_all,"id_use":id_use,"name":name,"Brands":ABrands
            })
def shoping(request):
    if request.user.is_authenticated:
        id_use = request.user.id
        name = request.user.username
        user = UserCustom.objects.get(user__id=id_use)
        sabad = models.sabad.objects.filter(id_user=id_use).count()
        product_all = models.Product.objects.all()
        ABrands = models.BrandMobile.objects.all()
        category = models.category.objects.all()
        saba = models.sabad.objects.all()
        return render(request, 'shopping.html',{"user":user,"sabad":sabad,"saba":saba,"category":category,"allp":product_all,"id_use":id_use,"name":name,"Brands":ABrands})
    else:
        redirect('/cart')