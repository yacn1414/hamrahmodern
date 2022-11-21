

from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.contrib import messages
from django.shortcuts import render,redirect
from main import models
from Users.models import UserCustom
from .models import comment
from main.models import Product,category,sabad,contact

# Create your views here.
def delete_address(request,id):
    if request.user.id == id:
        UserCustom.objects.filter(user__id=id).update(code_post="",fulladdress="")
        return redirect('/editAdderss')
def categories(request,c):
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
    "category.html"
    ,
    {"name":name,"id_use":id_use,"ofpr":Offrs,
    "category":category,"allp":product_all,
    "c":c,
    "ino":ino,"sabad":sabad,
    "saba":saba,"Brands":ABrands,"jamsabad":jamsabad}
    )
def pro(request,string):
    
    pro = Product.objects.get(name=string)
    # prod = Product.objects.all()

    if request.user.is_authenticated:
        id_use = request.user.id
        name = request.user.username
        sabad220 = len(sabad.objects.filter(id_user=request.user.id))
    else:
        id_use = 0
        name = None
        sabad220 = 0
    
    commentCount = len(comment.objects.filter(Product_id=pro.id))
    ABrands = models.BrandMobile.objects.all()
    jamsabad = models.jamsabad.objects.all()
    product_all = models.Product.objects.all()
    category = models.category.objects.all()
    saba = models.sabad.objects.all()

    color = models.colors.objects.filter(phoneid=pro.id)
    
    star = len(pro.star)
    if pro:
        return render(request,"product.html"
        ,{"name":name,"id_use":id_use,"colordb":color,
    "category":category,"allp":product_all,
    
    "sabad":sabad220,
    "star":star,
    "lencomment":commentCount,
    "saba":saba,"Brands":ABrands,"jamsabad":jamsabad,'pro':pro}
        )
    else:
        return HttpResponseNotFound("404") 

# def comment(request,id):
#     if request.method == "POST":
#         if request.user.is_authenticated:
#             a = request.POST['comment']
#             aa = models.comment.objects.create(text = a,user_id=request.user.id,username=request.user,Product_id=id)
            
#             messages.success(request,"کامنت شما ثبت شد")
#             return redirect(f"../pro/{id}")
#         else:
#             messages.warning(request,"شما هنوز عضو سایت نشدید ")
#             return redirect(f"../pro/{id}")

#     else:
#         return redirect(f"../pro/{id}")
def delete(request,id):
    if request.user.is_authenticated:    
        a = request.user.id
        res = sabad.objects.filter(id_pro=id,id_user=a).delete()
        if res !=0:
            return redirect("/cart")
            
    else:
        messages.info(request,"شما هنوز عضو سایت نشدید")
        redirect("/")
# def account(request):
    # if request.user.is_authenticated:
    #     id_use = request.user.username
    #     staff = request.user.is_superuser
    #     fullname = request.user.get_full_name
    #     phone = UserCustom.objects.get(user__username=id_use)
    # else:
    #     id_use = None
    #     return redirect('login')
    # return render(request, 'account.html',{"name":id_use,"staff":staff,"fullName":fullname,"phone":phone})
def buy(request):
    if request.method == 'POST':
        pass
    else:
        return redirect('/')
def editAddres(request):
    if request.user.is_authenticated:
        id_use = request.user.id
        name = request.user.username
        user = UserCustom.objects.get(user__id=id_use)
        sabad = models.sabad.objects.filter(id_user=id_use).count()
        product_all = models.Product.objects.all()
        ABrands = models.BrandMobile.objects.all()
        category = models.category.objects.all()
        saba = models.sabad.objects.all()
        return render(request, 'edit.html',{"user":user,"sabad":sabad,"saba":saba,"category":category,"allp":product_all,"id_use":id_use,"name":name,"Brands":ABrands})
    else:
        return redirect('/')