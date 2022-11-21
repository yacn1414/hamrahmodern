from . import views
from django.urls import path

urlpatterns = [
    path('',views.main),
    path('search',views.search),
    # path('likes/<id>',views.likes),
    path('confirm',views.shoping),
    path('cart/',views.sabad),
    path('seller/',views.sellers),
    path('sabad/<str:id>',views.sabad),
    
]
