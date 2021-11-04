from django.urls import path
from . import views

app_name = "acc"
urlpatterns = [
    path('', views.index, name="index"),
    path('login', views.userlogin, name="userlogin"),
    path('logout', views.userlogout, name="userlogout"),
    path('signup', views.signup, name="signup"),
    path('info', views.userinfo, name="userinfo"),
    path('del', views.userdel, name="userdel"),
    path('mod', views.usermod, name="usermod")
]