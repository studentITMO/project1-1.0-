from urllib import request
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate


from .models import myLinks

def index(request):
    
   return render(request, 'main/index.html') 
    

def auth(request):
    pass
    

def reg(request):
    if request.method == "POST":
        res = request.POST
        user = authenticate(username = res["last_login"],password = res["password"])
        print(user)
        
        if user != None:
            return redirect("http://127.0.0.1:8000/links/")
        elif user == None:
            createuser = User.objects.create_user(res["last_login"],"test",res["password"])
            createuser.save()
            redirect("http://127.0.0.1:8000/index/")
    return render(request, 'main/reg.html')

def links(request):
    data = myLinks.objects.all()
    print(data)

    return render(request, 'main/links.html', {'link': data})