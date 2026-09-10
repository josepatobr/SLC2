from django.shortcuts import render
from stock.models import Product
from django.conf import settings


def home(request):
    products = Product.objects.all()   
    context = {
        "products": products,
        "STREAMLIT_URL": settings.STREAMLIT_URL,
    } 
    return render(request, "home.html", context)


def dev(request):
    return render(request, "dev.html")


def search(request):
    input_search = request.POST.get("input_navbar")
    search_database = Product.objects.filter(name_product__icontains=input_search)
    if not search_database.exists():
        return render(request, "search_erro.html")
    else:
        return render(request, "search_sucess.html", {"search_database":search_database})
