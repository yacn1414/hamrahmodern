from django.urls import path
from . import views
app_name = "details"
urlpatterns = [
    path('product/<str:string>',views.pro),
    path('del/<int:id>',views.delete),
 
]
