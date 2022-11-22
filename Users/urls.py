from django.urls import path
from . import views
urlpatterns = [

    path('verify',views.verify),
    path('auth',views.auth,name="auth"),
    path('register',views.signup),
    path('login',views.loginUser,name='login'),
    path('authlogin',views.authlogin,name="authlogin"),
    path('profile',views.complete),
    path('Done',views.Done),
    path('account',views.profile),
    path('sefaresh',views.sefaresh),
    
]
