
from django.urls import path,include
#from django.urls import include, url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    #path('', views.user_login, name='user_login'),
    #path('login', 'django.contrib.auth.views.login',name='login'),
    #path('logout','django.contrib.auth.views.logout',name='logout'),
    #path('logout-then-login','django.contrib.auth.views.logout_then_login',name='logout-then-login')
    path('',views.dashboard, name='dashboard'),

   


]