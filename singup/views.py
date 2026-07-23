from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib import messages
from django.shortcuts import redirect
from .models import UserSingUp


def singup(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email") 
        password = request.POST.get("password")

        if len(name) <= 3 or len(password) <= 3:
            messages.error(request, "O nome ou senha precisa ter mais de 3 letras.")
            return redirect('singup')
        
        if UserSingUp.objects.filter(username=name).exists():
            messages.error(request, "Este nome de usuário já está em uso.")
            return redirect('singup')

        UserSingUp.objects.create_user(username=name, email=email, password=password)
        
        messages.success(request, "Conta criada com sucesso!")
        return redirect('home')
        
    return render(request, "singup.html")

def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    elif request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        
        messages.error(request, 'Nome ou senha inválidos.')
        return redirect('login')