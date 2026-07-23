from django.shortcuts import render
from stock.models import Product


def product_home(request):
    products =  Product.objects.all().select_related('company_name')
    products_in_stock = Product.objects.filter(product_status='IN_STOCK')
    
    return render(request, "home.html")

def product_view(request):
    product_view_id = Product.id()
    return render(request, f"product_pag.html{product_view_id:Product.id}")