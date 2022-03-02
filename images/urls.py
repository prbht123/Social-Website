from django.urls import path,include,re_path
#from django.urls import include, url

from . import views

app_name='images'

urlpatterns = [
    path('create/', views.image_create, name='create'),
]


