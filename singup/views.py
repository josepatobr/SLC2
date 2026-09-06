from django.shortcuts import render
from django.contrib.auth import authenticate
from .models import UserSingUp
import json
from django.http import JsonResponse


def singup(request):  
    if request.method == 'GET':
        return render(request, "singup.html")

    if request.method == "POST":
        try:
            data = json.loads(request.body)
            name = data.get("name")
            email = data.get("email")
            password = data.get("password")

            if UserSingUp.objects.filter(email=email).exi():
                return JsonResponse({'sucess':False, 'erro':'este email ja esta sendo usado em outra conta'})

            UserSingUp.objects.create(
                name=name,
                email=email,
                password=password
            )
            return json({"sucess": True})

        except Exception as e:
            return JsonResponse({'sucesso': False, 'erro': str(e)})

        
def login(request):
    if request.method == "GET":
        return render(request, "login.html")

    if request.method == "POST":
        try:
            data = json.loads(request.body)
            email = data.get("email")
            password = data.get("password")

            user = authenticate(request, email=email, password=password)
            if user is None:
                return JsonResponse({'sucess': False, 'erro': 'Credenciais inválidas'})
            return JsonResponse({"sucess": True})
        except Exception as e:
            return JsonResponse({"sucess": False, "erro":str(e)})
