from django.urls import path
from . import views
app_name = "details"
urlpatterns = [
    path('product/<str:string>',views.pro),
    path('del/<int:id>',views.delete),
    path('c/<str:c>',views.categories),
    path('buy',views.buy),
    path('editAddres',views.editAddres),
    path('delete_address/<int:id>',views.delete_address)
]
