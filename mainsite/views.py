from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def index(request):
    context = {}
    return render(request,"mainsite/index.html",context)

def sign_up(request):
    context ={}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request,user)
            return render(request,"investor/index.html")
    context['form'] = form
    return render(request,"mainsite/signup.html")


def login(request):
    context={}




