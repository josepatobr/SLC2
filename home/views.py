from django.shortcuts import render
from stock.models import Product 



#essa def é algo simples, ela apenas mostrara todos os produtos que tem no banco de dados e mostrara para o user
def home(request):
    products = Product.objects.all()    
    return render(request, "home.html", {'products':products})


