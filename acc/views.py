from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User

# Create your views here.
def index(request):
    return render(request, "acc/index.html")

def userlogin(request):
    un = request.POST.get("username")
    pw = request.POST.get("password")
    user = authenticate(username=un, password=pw)
    if user:
        login(request, user)
    return redirect("acc:index")

def userlogout(request):
    logout(request)
    return redirect("acc:index")

def signup(request):
    if request.method == "POST":
        un = request.POST.get("username")
        pw = request.POST.get("password")
        com = request.POST.get("comment")
        pic = request.FILES.get("pic")
        User.objects.create_user(username=un, password=pw, comment=com, pic=pic)
        return redirect("acc:index")
    return render(request, "acc/signup.html")

def userinfo(request):
    return render(request, "acc/userinfo.html")

def userdel(request):
    u = User.objects.get(username=request.user.username)
    u.delete()
    return redirect("acc:index")

def usermod(request):
    if request.method == "POST":
        un = request.user.username
        u = User.objects.get(username=un)
        pw = request.POST.get("password")
        pic = request.FILES.get("pic")
        com = request.POST.get("comment")
        if pw:
            u.set_password(pw)
        if pic:
            u.pic = pic
        u.comment = com
        u.save()
        user = authenticate(username=u, password=pw)
        login(request, user)
        return redirect("acc:userinfo")

    return render(request,"acc/usermod.html")