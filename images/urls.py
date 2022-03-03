from django.urls import path,include,re_path
#from django.urls import include, url

from . import views

app_name='images'

urlpatterns = [
    path('create/', views.image_create, name='create'),
    path('detail/<int:id>+)/<str:slug>/',views.image_detail, name='detail'),
    path('like/', views.image_like, name='like'),
 #   path('', views.image_list, name='list'),
]


