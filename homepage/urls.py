from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home, name="home",),
    path('about', views.About, name="about"),
    path('upload', views.upload, name="upload"),
    path('login', views.login_page, name="login"),
    path('signup', views.signup_user, name="signup"),
    path('logout', views.logout_user, name="logout"),
    path('custupload', views.custupload, name="custupload"),
    path('watch', views.watch, name="watch"),
    path('laptop', views.laptop, name="laptop"),
    path('mobile', views.mobile, name="mobile"),
    path('graphic', views.graphic, name="graphic"),
    path('processor', views.processor, name="processor"),
    path('accessory', views.accessory, name="accessory")
]
