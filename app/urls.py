from django.contrib import admin
from django.urls import path,re_path
from app import views

app_name="app"

urlpatterns = [
     path('sslc/', views.post_list_sslc, name='post_list_sslc'),
    path('puc/',views.post_list_puc, name='post_list_puc'),
    path('engg/',views.post_list_engg, name='post_list_engg'),
    path('masters/',views.post_list_masters, name='post_list_masters'),
    path('post/<int:pk>/',views.post_detail_sslc, name='post_detail_sslc'),
    path('pu/<int:pk>/',views.post_detail_puc, name='post_detail_puc'),
    path('en/<int:pk>/',views.post_detail_engg, name='post_detail_engg'),
    path('ms/<int:pk>/',views.post_detail_masters, name='post_detail_masters'),
    path('register/',views.register,name='register'),
    path('login/',views.user_login,name='login'),
]