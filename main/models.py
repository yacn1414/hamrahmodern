from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from django.db import models
class Offer(models.Model):
    time = models.DateTimeField(_("زمان تخفیف"))
    darsad = models.IntegerField(_("درصد تخفیف"))
    def __str__(self):
        return str(self.darsad)
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'تخفیف ها '

    


class Product(models.Model):
    NUMBERS = [
        ("1", 1),
        ("22", 2),
        ("333", 3),
        ("4444", 4),
        ("55555", 5),
    ]

    
    name = models.CharField(_("اسم محصول"),max_length=255,unique=True)
    price = models.IntegerField(_("قیمت به تومان"))
    picture = models.ImageField(_("عکس نمایشی"),upload_to='ProductImage/picture')
    picture2 = models.ImageField(_("عکس پیش نمایش"),upload_to='ProductImage/picture2')
    picture3 = models.ImageField(_("عکس جزيیات"),upload_to='ProductImage/picture3')
    picture4 = models.ImageField(_("عکس جزییات"),upload_to='ProductImage/picture4')
    vip = models.CharField(_("محصول ویژه"),max_length=20,default="no",choices=[("no","خیر"),("yes","بله")])
    price_offer = models.ForeignKey(Offer,on_delete = models.CASCADE,blank=True,null=True,default=0)
    category = models.ForeignKey("BrandMobile",on_delete=models.CASCADE)
    star = models.CharField(_("امتیاز به ستاره"),max_length=25,choices=NUMBERS)
    caption = models.TextField(_("معرفی جزیَی"),)
    detail = models.TextField(_("معرفی دقیق"),)
    buyers = models.IntegerField(_("تعداد فروش"),default=0)
    view = models.IntegerField(_("تعداد بازدید"),default=0)

    mojood = models.CharField(max_length=20,default="موجود",choices=[("موجود","ناموجود")])
    def __str__(self):
        return str(self.name)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'محصولات'
        verbose_name_plural = 'محصولات'
class colors(models.Model):
    COLOR = [
        ("white","white"),
        ("black","black"),
        ("gray","gray"),
        ("yellow","yellow"),
        ("blue","blue"),
        ("red","red"),
        ("gold","gold"),
        ("silwer","silwer"),
        # ("",""),
        # ("",""),

    ]
    color = models.CharField(max_length=255,choices=COLOR)
    code = models.CharField(max_length=255)
    phoneid = models.ForeignKey("Product", on_delete=models.CASCADE)
    def __str__(self):
        return self.code

class Email(models.Model):
    Email = models.EmailField(blank=False,unique=True)
    def __str__(self):
        return str(self.Email)
class category(models.Model):
    nameFa = models.CharField(_("اسم "),max_length=255)
    nameEn = models.CharField(_("اسم انگلیسی"),max_length=255)
    def __str__(self):
        return self.nameEn
class BrandMobile(models.Model):
    nameEn = models.CharField(_("اسم انگلیسی"),max_length=255)
    Tpost = models.IntegerField(_("تعداد پست"),default=0)
    image = models.ImageField(_("عکس "),upload_to="category")
    name = models.CharField(_("اسم "),max_length=255)
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class interest(models.Model):
    id_pro = models.IntegerField()
    id_user = models.IntegerField(blank=True,null=True)
    class Meta:
        verbose_name_plural = _("علاقمندی ها")
        verbose_name = _("علاقمندی ها")
class sabad(models.Model):
    id_pro = models.IntegerField()
    T = models.IntegerField(_("تعداد"),default=1)
    id_user = models.IntegerField(blank=True,null=True)
    p = models.CharField(max_length=255)
    p2 = models.CharField(max_length=255)
    color = models.CharField(max_length=255,default="black")
class jamsabad(models.Model):
    jam = models.IntegerField(blank=True,null=True)
    id_user = models.IntegerField()
    # def __str__(self):
    #     return self.jam

class contact(models.Model):
    username = models.CharField(max_length=30)
    textmessage = models.TextField()
    response = models.TextField(null=True,blank=True)
    class Meta:
        verbose_name = _("contact")
        verbose_name_plural = _("contact")

    def __str__(self):
        return self.username
from django.dispatch import receiver
from django.db.models.signals import post_save,post_delete
@receiver(post_save,sender=Product)
def add_to_category(sender,instance,created,**kwargs):
    if created:
        b = BrandMobile.objects.get(id=instance.category.id)
        b.Tpost += 1
        b.save()


@receiver(post_delete,sender=Product)
def delete_category(sender,instance,**kwargs):
    b = BrandMobile.objects.get(id=instance.category.id)
    b.Tpost -= 1
    b.save()


