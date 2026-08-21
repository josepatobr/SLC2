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

 
