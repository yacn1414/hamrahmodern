

from django.shortcuts import render
# from django.http import HttpResponseNotFound,JsonResponse
from django.contrib import messages
from django.shortcuts import render,redirect
from . import models

from main.models import Product,category,sabad,contact

# Create your views here.
# def edit(request):
#     a = {
#         "name" : request.POST['fullname'],
#         "email" : request.POST['email'],
        
#         "state" : request.POST['state'],
#     }
#     return JsonResponse(a)
# def about(request):
#     # half
#     return render(request,'about.html',{})
    
# def editaccount(request):
#     return render(request, 'edit.html')
# def security(request):
#     pass
# def categoryview(request,parametr):
    # return HttpResponse(f"ok {parametr}")
def pro(request,string):
    
    pro = Product.objects.get(name=string)
    # prod = Product.objects.all()
    saba = sabad.objects.all()
    if request.user.is_authenticated:
        id_use = request.user.id
    else:
        id_use = 0
    # cate = category.objects.all()
    # if request.user.is_authenticated:
        
    #     sabad1 = len(sabad.objects.filter(id_user=request.user.id))
    #     ino = len(interest.objects.filter(id_user=request.user.id))
    # else:
    #     sabad1 = 0
    #     ino = 0
    # co = models.comment.objects.all()

    # buyful = Product.objects.all().order_by('buyers')[:10]
    # commentCount = len(models.comment.objects.filter(Product_id=id))
    if pro:
        return render(request,"product.html"
        ,{"pro":pro,"id_use":id_use,"saba":saba,
    # "category":cate,"allp":prod,"banner":banner,"comcount":commentCount,"comments":co,"sabad":sabad1,"ino":ino,"buy":buyful
            }
        )
    else:
        return HttpResponseNotFound("404") 
# def next(request,id):
#     try:
#         if Product.objects.get(id=int(id)+1):
#             return redirect(f"/pro/{int(id)+1}")
#     except:
#         for i in range(1,100):
#             a = Product.objects.filter(id=i)
#             if a:
#                 return redirect(f"/pro/{i}")

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
# def delete(request,id):
#     if request.user.is_authenticated:    
#         a = request.user.id
#         sabad.objects.filter(id_pro=id,id_user=a).delete()
#         return redirect("/sabad")
#     else:
#         messages.info(request,"شما هنوز عضو سایت نشدید")
#         redirect("../")
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