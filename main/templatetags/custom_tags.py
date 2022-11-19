from django.db.models import ExpressionWrapper,F,DecimalField
from django.http import HttpResponse
from django import template

from main.models import sabad,jamsabad
register = template.Library()
@register.simple_tag
def takhfif(price, price_offer, *args, **kwargs):
    resualt = int((price/100)*int(str(price_offer)[0:2])-price)*-1
    

    return f"{resualt:,}"

@register.simple_tag
def jam(price,price_offer, t,*args, **kwargs):
    a = ""
    for i in takhfif(price,price_offer).split(","):
        a += i
    
    resualt = int(a) * t
    return f"{resualt:,}"
@register.simple_tag
def format(resualt,*args, **kwargs):
    return f"{resualt:,}"
@register.simple_tag
def jam3(id_use, *args, **kwargs):
    a = 0
    saba = sabad.objects.filter(id_user = id_use)
    for dataSabad in saba:
        a += jam2(dataSabad.p2,dataSabad.T)
    
    return f"{a:,}"
@register.simple_tag
def jam4(id_use, *args, **kwargs):
    a = 0
    saba = sabad.objects.filter(id_user = id_use)
    for dataSabad in saba:
        a += jam2(dataSabad.p2,dataSabad.T)
    b = a + 25000
    return f"{b:,}"

@register.simple_tag
def jam2(p,t, *args, **kwargs):
    a = p.replace(",","")
    res = int(a) * int(t)
    return int(res)
@register.simple_tag
def res(id_use, *args, **kwargs):
    a = jamsabad.objects.filter(id_user=id_use)
    count = 0
    for mmd in a:
        count += mmd.jam
    if count:
        return f"{count:,}"
    else:
        return 0
@register.simple_tag
def nerkhasli(id_use, *args, **kwargs):
    if id_use :
        a = sabad.objects.filter(id_user=id_use)
        ab=0
        for mm in a:
            ab += int(mm.p2)
        return f"{ab:,}"
@register.simple_tag
def jampost(id_use, *args, **kwargs):
    a = jamsabad.objects.filter(id_user=id_use)
    count = 0
    for mmd in a:
        count += mmd.jam
    if count:
        return f"{count+25000:,}"
    else:
        return 0